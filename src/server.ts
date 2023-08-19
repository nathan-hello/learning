import jwt from "jsonwebtoken";
import express from "express";
import type { Request, Response, NextFunction, RequestHandler } from "express";
import bcrypt from "bcrypt";
import { config, logger } from "./config";
import { custom, z } from "zod";
import { prismaConstructor, responseSchema, requestSchema } from "./db";
import { Prisma, PrismaClient } from "@prisma/client";
import { BadBody, BadId, BadRegistryInfo, WrongCredentialsException, middlewares } from "./middle";
import { networkInterfaces } from "os";
import { match } from "assert";
import { nextTick } from "process";



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

class AuthController implements Controller {
    public path = "/auth";
    public router = express.Router();

    constructor(public db: PrismaClient) {
        this.db = db;
        this.router.post(`${this.path}/register`, this.postRegister);
        this.router.post(`${this.path}/login`, this.postLogin);
    }

    private postRegister: RequestHandler = async (req, res, next) => {
        const newUser = requestSchema.user.safeParse(req.body);
        if (!newUser.success) {
            next(new BadRegistryInfo());
            return;
        }
        const checkUserExists = await this.db.user.findFirst({ where: { email: newUser.data.email } });
        if (checkUserExists) {
            next(new BadRegistryInfo());
            return;
        }

        const hashedPassword = await bcrypt.hash(newUser.data.password, 10);
        const upload = await this.db.user.create({
            data: {
                email: newUser.data.email,
                password: hashedPassword
            }
        });
        res.json({ email: `${upload.email}` });
        return;
    };

    private postLogin: RequestHandler = async (req, res, next) => {
        const loginData = requestSchema.user.safeParse(req.body);
        if (!loginData.success) {
            next(new WrongCredentialsException());
            return;
        }

        const user = await this.db.user.findUnique({ where: { email: loginData.data.email } });
        if (!user) {
            next(new WrongCredentialsException());
            return;
        }

        const matchPassword = await bcrypt.compare(loginData.data.password, user.password);
        if (!matchPassword) {
            next(new WrongCredentialsException());
            return;
        }

        res.json({ email: loginData.data.email });
        return;
    };
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


    private get: RequestHandler = async (req, res, next) => {
        var offset = 0;
        var limit = 5;
        if (req.query.offset) {
            var offset = z.coerce.number().min(0).parse(req.query.offset);
        }
        if (req.query.limit) {
            var limit = z.coerce.number().max(20).parse(req.query.limit);
        }

        const posts = await this.db.post.findMany({
            take: limit,
            orderBy: { id: "asc" },
            where: { id: { gte: offset, lte: offset + limit } }
        });
        res.send(posts);
        return;
    };

    private post: RequestHandler = async (req, res, next) => {
        const post = requestSchema.post.safeParse(req.body);
        if (!post.success) {
            next(new BadBody(post.error.message));
            return;
        }
        const newPost = await this.db.post.create({
            data: post.data
        });
        res.send({ id: newPost.id });
        return;

    };

    private getById: RequestHandler = async (req, res, next) => {
        const id = z.coerce.number().safeParse(req.params.id);
        if (!id.success) {
            next(new BadId());
            return;
        }
        const result = await this.db.post.findUnique({ where: { id: id.data } });
        if (!result) {
            res.sendStatus(404);
            return;
        }
        res.json(result);
        return;

    };

    private patchById: RequestHandler = async (req, res, next) => {
        const id = z.coerce.number().safeParse(req.params.id);
        if (!id.success) {
            next(new BadId());
            return;
        }
        const findPost = await this.db.post.findUnique({ where: { id: id.data } });
        if (!findPost) {
            next(new BadId());
            return;
        }

        const newPost = requestSchema.post.safeParse(req.body);
        if (!newPost.success) {
            next(new BadBody(newPost.error.message));
            return;
        }

        const update = await this.db.post.update({
            where: { id: findPost.id }, data: {
                title: newPost.data.title,
                content: newPost.data.content,
                author: newPost.data.author
            }
        });

        res.json(update);
        return;
    };

    private deleteById: RequestHandler = async (req, res, next) => {
        const id = z.coerce.number().safeParse(req.params.id);
        if (!id.success) {
            next(new BadId());
            return;
        }
        const findPost = await this.db.post.findUnique({ where: { id: id.data } });
        if (!findPost) {
            next(new BadId());
            return;
        }

        const deleted = await this.db.post.delete({ where: { id: findPost.id } });
        res.json({ id: deleted.id });
        return;
    };
};





class App {
    public app: express.Application;
    public config = config;

    constructor(controllers: Controller[]) {
        this.app = express();
        this.initializeControllers(controllers);
    }

    private initializeControllers(controllers: Controller[]) {
        controllers.forEach(c => {
            this.app.use(middlewares.logging);
            this.app.use(express.json());
            this.app.use(express.text());
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