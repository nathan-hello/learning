import jwt from "jsonwebtoken";
import express from "express";
import type { Request, Response, NextFunction } from "express";
import bcrypt from "bcrypt";
import { config, logger } from "./config";
import { custom, z } from "zod";
import { prismaConstructor, schema } from "./db";
import { Prisma, PrismaClient } from "@prisma/client";


interface Controller {
    path: string,
    router: express.Router;
    db: PrismaClient;
    initalizeRoutes(): void;
}

class IndexController implements Controller {
    public path = "/";
    public router = express.Router();

    constructor(public db: PrismaClient) {
        this.initalizeRoutes();
        this.db = db;
    }

    public initalizeRoutes() {
        this.router.get(this.path, this.get);
    }

    get = (_req: Request, res: Response) => res.status(200).send({ message: "Hello!" });
}

class PostsController implements Controller {
    public path = '/posts';
    public router = express.Router();

    constructor(public db: PrismaClient) {
        this.db = db;
        this.initalizeRoutes();
    }

    public initalizeRoutes() {
        this.router.get(this.path, this.get);
        this.router.post(this.path, this.post);
    }


    get = async (_req: express.Request, res: express.Response) => {
        const allPosts = await this.db.post.findMany();
        res.send(allPosts);
    };

    post = async (req: express.Request, res: express.Response) => {
        const post = schema.post.safeParse(req.body);
        if (post.success) {
            await this.db.post.create({
                data: post.data
            });
            res.status(200).send(post.data);
        } else {
            res.status(405).send(post.error);
        }
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