import { getCollection } from 'astro:content';

export async function getBlogPosts() {
    const posts = await getCollection('blog');
    return posts.sort((a, b) => b.data.date.getTime() - a.data.date.getTime());
}

export async function getPostBySlug(slug: string) {
    const posts = await getCollection('blog');
    return posts.find(post => post.id === slug);
}
