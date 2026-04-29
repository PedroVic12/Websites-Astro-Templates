import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const viagem = defineCollection({
    loader: glob({
        pattern: '**/*.md',
        base: 'src/content/viagem',
    }),
    schema: z.object({
        title: z.string(),
        destination: z.string(),
        origin: z.string(),
        base: z.string(),
        logistics: z.object({
            route: z.array(z.string()),
            time: z.string(),
            tips: z.array(z.string()),
        }),
        days: z.array(z.object({
            day: z.number(),
            title: z.string(),
            focus: z.string(),
            events: z.array(z.object({
                time: z.string(),
                desc: z.string(),
                icon: z.string(),
            })),
        })),
        images: z.array(z.string()),
    }),
});

export const collections = { viagem };