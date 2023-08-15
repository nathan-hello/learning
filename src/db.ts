import { Prisma, PrismaClient } from "@prisma/client";
import fs from "fs";
import { logger } from "./config";
import { z } from "zod";

export const schema = {
    post: z.object({
        author: z.string(),
        content: z.string(),
        title: z.string(),
        date: z.date().default(new Date())
    })
};


export function prismaConstructor() {
    const prisma = new PrismaClient({
        log: [
            { level: "query", emit: "event" },
            { level: "info", emit: "event" },
            { level: "warn", emit: "event" },
            { level: "error", emit: "event" }
        ]
    });

    prisma.$on("query", (e) => {
        logger.log("info", `${e.timestamp} | ${e.query} | ${e.params} | ${e.target} | ${e.duration}`);
    });
    prisma.$on("info", (e) => {
        logger.log("info", `PRISMA: ${e.message} | ${e.target}`);
    });
    prisma.$on("warn", (e) => {
        logger.log("warn", `PRISMA: ${e.timestamp} | ${e.message} | ${e.target}`);
    });
    prisma.$on("error", (e) => {
        logger.log("error", `PRISMA: ${e.timestamp} | ${e.message} | ${e.target}`);
    });
    return prisma;
}
