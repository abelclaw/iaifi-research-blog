/**
 * Precompute t-SNE and PCA coordinates for the scatter plot.
 * Run: node scripts/compute-scatter.cjs
 * Output: src/data/scatter-coords.json
 */
const fs = require("fs");
const path = require("path");

async function main() {
  // Load concepts data
  const conceptsPath = path.join(__dirname, "../src/data/concepts.json");
  if (!fs.existsSync(conceptsPath)) {
    console.log("No concepts.json found, skipping scatter precompute.");
    process.exit(0);
  }
  const conceptEntries = JSON.parse(fs.readFileSync(conceptsPath, "utf-8"));
  console.log(`Loaded ${conceptEntries.length} papers`);

  // Build concept vocabulary
  const conceptSet = new Set();
  for (const entry of conceptEntries) {
    for (const c of (entry.concepts || [])) conceptSet.add(c);
  }
  const conceptVocab = Array.from(conceptSet).sort();
  const conceptIdx = new Map(conceptVocab.map((c, i) => [c, i]));
  console.log(`Vocabulary: ${conceptVocab.length} concepts`);

  // Build relevance lookup
  const relevanceMap = {};
  for (const entry of conceptEntries) {
    relevanceMap[entry.arxivId] = {};
    for (const cd of (entry.conceptDetails || [])) {
      relevanceMap[entry.arxivId][cd.name] = cd.relevance || 0;
    }
  }

  // Build feature matrix
  const featureMatrix = conceptEntries.map((entry) => {
    const row = new Array(conceptVocab.length).fill(0);
    for (const c of (entry.concepts || [])) {
      const idx = conceptIdx.get(c);
      if (idx !== undefined) {
        row[idx] = (relevanceMap[entry.arxivId] || {})[c] || 0.5;
      }
    }
    return row;
  });

  // PCA
  console.log("Computing PCA...");
  const { PCA } = require("ml-pca");
  const pca = new PCA(featureMatrix);
  const pcaResult = pca.predict(featureMatrix, { nComponents: 2 });
  const pcaCoords = pcaResult.to2DArray();
  console.log("PCA done");

  // First reduce to 50 dims with PCA for faster t-SNE
  console.log("Computing PCA-50 for t-SNE input...");
  const pcaReduced = pca.predict(featureMatrix, { nComponents: 50 });
  const reducedMatrix = pcaReduced.to2DArray();

  // t-SNE
  console.log("Computing t-SNE (this may take a minute)...");
  const TSNE = require("tsne-js");
  const tsneModel = new TSNE({
    dim: 2,
    perplexity: Math.min(30, Math.floor(conceptEntries.length / 4)),
    earlyExaggeration: 4.0,
    learningRate: 200,
    nIter: 500,
    metric: "euclidean",
  });
  tsneModel.init({ data: reducedMatrix, type: "dense" });
  tsneModel.run();
  const tsneCoords = tsneModel.getOutputScaled();
  console.log("t-SNE done");

  // Build output: arxivId -> { pca, tsne }
  const coords = {};
  for (let i = 0; i < conceptEntries.length; i++) {
    coords[conceptEntries[i].arxivId] = {
      pca: [Math.round(pcaCoords[i][0] * 10000) / 10000, Math.round(pcaCoords[i][1] * 10000) / 10000],
      tsne: [Math.round(tsneCoords[i][0] * 10000) / 10000, Math.round(tsneCoords[i][1] * 10000) / 10000],
    };
  }

  const outPath = path.join(__dirname, "../src/data/scatter-coords.json");
  fs.writeFileSync(outPath, JSON.stringify(coords));
  console.log(`Wrote ${Object.keys(coords).length} entries to ${outPath}`);

  // --- Build full scatter-data.json for the client ---
  console.log("Building scatter-data.json...");

  // Institution data now comes directly from concepts.json (exported by pipeline)
  // No need to load iaifi-members.json separately

  // Institution frequency across papers
  const instFreq = {};
  for (const entry of conceptEntries) {
    const inst = entry.institution || null;
    if (inst) instFreq[inst] = (instFreq[inst] || 0) + 1;
  }
  const topInstitutions = Object.entries(instFreq)
    .sort((a, b) => b[1] - a[1])
    .map(([name, count]) => ({ name, count }));
  console.log(`Institutions: ${topInstitutions.map(i => `${i.name}(${i.count})`).join(", ")}`);

  // Concept frequency
  const conceptFreq = {};
  for (const entry of conceptEntries) {
    for (const c of (entry.concepts || [])) {
      conceptFreq[c] = (conceptFreq[c] || 0) + 1;
    }
  }
  const topConcepts = Object.entries(conceptFreq)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 200)
    .map(([name, count]) => ({ name, count }));

  // Author frequency
  const authorFreq = {};
  for (const entry of conceptEntries) {
    for (const a of (entry.authors || [])) {
      authorFreq[a] = (authorFreq[a] || 0) + 1;
    }
  }
  const topAuthors = Object.entries(authorFreq)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 100)
    .map(([name, count]) => ({ name, count }));

  // Concept -> paper index, Author -> paper index
  const topConceptNames = new Set(topConcepts.map((c) => c.name));
  const topAuthorNames = new Set(topAuthors.map((a) => a.name));
  const conceptIndex = {};
  const authorIndex = {};
  for (let i = 0; i < conceptEntries.length; i++) {
    const entry = conceptEntries[i];
    if (!coords[entry.arxivId]) continue;
    for (const c of (entry.concepts || [])) {
      if (topConceptNames.has(c)) {
        (conceptIndex[c] = conceptIndex[c] || []).push(i);
      }
    }
    for (const a of (entry.authors || [])) {
      if (topAuthorNames.has(a)) {
        (authorIndex[a] = authorIndex[a] || []).push(i);
      }
    }
  }

  // Institution -> paper index
  const institutionIndex = {};
  for (let i = 0; i < conceptEntries.length; i++) {
    const entry = conceptEntries[i];
    if (!coords[entry.arxivId]) continue;
    const inst = entry.institution || null;
    if (inst) {
      (institutionIndex[inst] = institutionIndex[inst] || []).push(i);
    }
  }

  // Papers array (minimal)
  const papers = conceptEntries
    .filter((e) => coords[e.arxivId])
    .map((e) => ({
      id: e.arxivId,
      title: e.title,
      nick: e.nickname || null,
      theme: e.theme,
      year: e.published ? new Date(e.published).getFullYear() : null,
      slug: e.blogSlug || null,
      cc: (e.concepts || []).length,
      a: (e.authors || []).slice(0, 4),
      inst: e.institution || null,
      pca: coords[e.arxivId].pca,
      tsne: coords[e.arxivId].tsne,
    }));

  const scatterData = { papers, topConcepts, topAuthors, topInstitutions, conceptIndex, authorIndex, institutionIndex };
  const scatterPath = path.join(__dirname, "../src/data/scatter-data.json");
  fs.writeFileSync(scatterPath, JSON.stringify(scatterData));
  console.log(`Wrote scatter-data.json (${papers.length} papers, ${Math.round(fs.statSync(scatterPath).size / 1024)}KB)`);
}

main().catch((e) => { console.error(e); process.exit(1); });
