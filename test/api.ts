import { z } from "zod";
import { responseSchema } from "../src/db";

const baseUrl = "http://localhost:3000";

async function testPostsController() {

    const p = 1;

    const getPosts = await fetch(`${baseUrl}/posts`)
        .then(r => r.json())
        .then(v => z.array(responseSchema.getPostById).parse(v))
        .then((c) => { console.log(`/posts GET length: ${c.length}`); return c; });

    const postPosts = await fetch(`${baseUrl}/posts`, {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            author: "hugh",
            content: "grant's",
            title: "liver"
        })
    })
        .then(p => p.json())
        .then(j => responseSchema.postIdObject.parse(j))
        .then((v) => { console.log(`/posts POST: ${v.id}`); return v; });

    const getPostById = await fetch(`${baseUrl}/posts/${p}`, {
        method: "GET",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json",
        },

    })
        .then(r => r.json())
        .then(v => responseSchema.getPostById.parse(v))
        .then(c => { console.log(`/posts/${p} GET id: ${c.id}`); return c; });

    const patchPost = await fetch(`${baseUrl}/posts/${p}`, {
        method: "PATCH",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            title: `1234`,
            content: "wormengensen",
            author: "heyyyyoo"
        })
    })
        .then(r => r.json())
        .then(v => responseSchema.getPostById.parse(v))
        .then(c => { console.log(`/posts/${p} PATCH: updated ${c.id}'s title from ${getPostById.title} to ${c.title}`); return c; });

    const deletePost = await fetch(`${baseUrl}/posts/${postPosts.id}`, {
        method: "DELETE",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    })
        .then(r => r.json())
        .then(v => responseSchema.postIdObject.parse(v))
        .then(c => { console.log(`/post/${postPosts.id} DELETE: id: ${c.id}`); return c; });


}

testPostsController();
