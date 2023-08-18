import { z } from "zod";
import { schema } from "../src/db";

const baseUrl = "http://localhost:3000";

async function testPostsController() {
    const posts = await fetch(`${baseUrl}/posts`).then(r => r.json());
    const validatePosts = z.array(schema.downstream.post).safeParse(posts);
    console.log(`/posts successful: ${validatePosts.success} `);

    const newPost = await fetch(`${baseUrl}/posts`, {
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
    });

    // console.log(`/posts POST: ${JSON.stringify(newPost.body)}`);
    console.log(`/posts POST: ${JSON.stringify(await newPost.json())}`);
}

testPostsController();
console.log("bye");;