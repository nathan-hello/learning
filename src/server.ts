import jwt from "jsonwebtoken";
import express from "express";
import type { Request, Response, NextFunction } from "express";
import bcrypt from "bcrypt";
import { config, logger } from "./config";
import { custom, z } from "zod";
import { prismaConstructor, schema } from "./db";
import { Prisma, PrismaClient } from "@prisma/client";
import e from "express";

type RouteHandler = (req: Request, res: Response, next?: NextFunction) => void;

interface Controller {
    path: string,
    router: express.Router;
    db: PrismaClient;
}

class IndexController implements Controller {
    public path = "/";
    public router = express.Router();

    constructor(public db: PrismaClient) {
        this.db = db;
        this.router.get(this.path, this.get);
    }

    private get = (_req: Request, res: Response) => res.status(200).send({ message: "Hello!" });
}

class PostsController implements Controller {
    public path = '/posts';
    public router = express.Router();

    constructor(public db: PrismaClient) {
        this.db = db;
        this.router.get(this.path, this.get);
        this.router.get(`${this.path}/:id`, this.getById);
        this.router.post(this.path, this.post);
        this.router.delete(`${this.path}/:id`, this.deleteById);
        this.router.patch(`${this.path}/:id`, this.patchById);
    }


    private get = async (_req: Request, res: Response) => {
        const allPosts = await this.db.post.findMany();
        res.send(allPosts);
    };

    private post = async (req: Request, res: Response) => {
        const post = schema.post.safeParse(req.body);
        if (!post.success) {
            res.status(405).send(post.error);
        } else {
            await this.db.post.create({
                data: post.data
            });
            res.status(200).send(post.data);
        }
    };

    private getById: RouteHandler = async (req, res) => {
        const id = z.number().parse(req.params.id);
        const result = await this.db.post.findUnique({ where: { id: id } });
        if (result === null) {
            res.status(404).send("Post not found");
        } else {
            res.status(200).send(result);
        }
    };

    private patchById: RouteHandler = async (req, res) => {
        const id = z.number().parse(req.params.id);
        const newPost = z.object({ content: z.string(), title: z.string() }).safeParse(req.body);
        if (!newPost.success) {
            res.status(400).send({
                message:
                    "Error: /posts/:id expects {content: string, title: string}. Data provided is in incorrect shape"
            });
        } else {
            this.db.post.update({ where: { id: id }, data: { title: newPost.data.title, content: newPost.data.content } });
        }
    };

    private deleteById: RouteHandler = async (req, res) => {
        const id = z.number().parse(req.params.id);
        const find = await this.db.post.findUnique({ where: { id: id } });
        if (!find) {
            res.status(400).send({ message: `Post at id ${id} not found` });
        } else {
            await this.db.post.delete({ where: { id: find.id } });
            res.status(200).send({ message: `Deleted post ${id}` });
        };
    };

}



class App {
    public app: express.Application;
    public config = config;
    public middlewares = {
        logger: (req: Request, _res: Response, next: NextFunction) => {
            logger.log("info", `REQUEST FROM IP: [${req.ip}] METHOD: [${req.method}] PATH: [${req.path}]`); next();
        },
        bodyParser: express.json()
    } as const;

    constructor(controllers: Controller[]) {
        this.app = express();
        this.initializeControllers(controllers);
    }

    private initializeControllers(controllers: Controller[]) {
        controllers.forEach(c => {
            this.app.use(this.middlewares.logger);
            this.app.use(this.middlewares.bodyParser);
            this.app.use("/", c.router);
        });
    }

    public listen() {
        this.app.listen(this.config.portListen, () => { console.log(`App started on port ${this.config.portListen}`); });
    }
}

const prisma = prismaConstructor();

const app = new App([
    new IndexController(prisma),
    new PostsController(prisma),
]);

app.listen();