import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const posts = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  schema: z.object({
    title: z.string(),
    arxivId: z.string(),
    authors: z.array(z.string()),
    abstract: z.string(),
    theme: z.enum([
      "Foundational AI",
      "Theoretical Physics",
      "Experimental Physics",
      "Astrophysics",
    ]),
    published: z.coerce.date(),
    arxivUrl: z.string().url(),
    pdfUrl: z.string().url(),
    concepts: z.array(z.string()),
    figures: z.array(z.string()).default([]),
    wordCount: z.number(),
  }),
});

export const collections = { posts };
