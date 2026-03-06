"""Fetch Paperscape map coordinates for IAIFI papers."""
import json
import urllib.request
import urllib.parse
import time
import sys
import re

def fetch_jsonp(url):
    """Fetch JSONP and extract the JSON payload."""
    req = urllib.request.Request(url, headers={"User-Agent": "IAIFI-Blog/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        text = resp.read().decode("utf-8")
    # Extract JSON from JSONP: callback({...})
    m = re.match(r'^[^(]+\((.+)\)\s*$', text, re.DOTALL)
    if m:
        return json.loads(m.group(1))
    return json.loads(text)

def main():
    # Load IAIFI papers
    with open("site/src/data/scatter-data.json") as f:
        data = json.load(f)

    papers = data["papers"]
    print(f"Fetching Paperscape coords for {len(papers)} papers...")

    # Fetch world index for bounds
    world = fetch_jsonp("http://tile1.paperscape.org/world/world_index.json")
    print(f"World bounds: x=[{world['xmin']}, {world['xmax']}], y=[{world['ymin']}, {world['ymax']}]")
    print(f"Total arXiv papers in Paperscape: {world['numpapers']}")

    results = []
    found = 0
    not_found = 0

    for i, paper in enumerate(papers):
        arxiv_id = paper["id"]
        try:
            # Use mr2l to get coordinates (returns x, y, r)
            url = f"http://paperscape.org/wombat?callback=cb&mr2l={urllib.parse.quote(arxiv_id)}&tbl="
            resp = fetch_jsonp(url)

            if resp.get("r") and resp["r"].get("papr") and len(resp["r"]["papr"]) > 0:
                p = resp["r"]["papr"][0]
                if p.get("x") is not None and p.get("y") is not None:
                    results.append({
                        "arxiv_id": arxiv_id,
                        "title": paper["title"],
                        "theme": paper["theme"],
                        "slug": paper.get("slug"),
                        "ps_id": p["id"],
                        "x": p["x"],
                        "y": p["y"],
                        "r": p.get("r", 10),
                        "nc": paper.get("cc", 0),
                    })
                    found += 1
                else:
                    not_found += 1
            else:
                not_found += 1
        except Exception as e:
            print(f"  Error for {arxiv_id}: {e}", file=sys.stderr)
            not_found += 1

        if (i + 1) % 20 == 0:
            print(f"  {i+1}/{len(papers)} processed ({found} found, {not_found} missing)")

        # Be polite to the server
        time.sleep(0.15)

    print(f"\nDone: {found} found, {not_found} not found out of {len(papers)}")

    output = {
        "world": {
            "xmin": world["xmin"],
            "ymin": world["ymin"],
            "xmax": world["xmax"],
            "ymax": world["ymax"],
        },
        "papers": results,
    }

    out_path = "site/src/data/paperscape-data.json"
    with open(out_path, "w") as f:
        json.dump(output, f)
    print(f"Wrote {out_path} ({len(results)} papers)")

if __name__ == "__main__":
    main()
