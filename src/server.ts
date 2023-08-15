import jwt from "jsonwebtoken";
import express from "express";
import type { Request, Response, NextFunction } from "express";
import bcrypt from "bcrypt";
import { config } from "./config";
import { z } from "zod";


interface Controller {
    path: string,
    router: express.Router;
    initalizeRoutes(): void;
}

class IndexController implements Controller {
    public path = "/";
    public router = express.Router();

    constructor() {
        this.initalizeRoutes();
    }
    public initalizeRoutes() {
        this.router.get(this.path, this.getIndex);

    }
    getIndex = (_req: Request, res: Response) => res.status(200).send({ status: "success" });
}

class PostsController implements Controller {
    public path = '/posts';
    public router = express.Router();
    public postSchema = z.object({
        author: z.string(),
        content: z.string(),
        title: z.string(),
    });

    private posts: z.infer<typeof this.postSchema>[] = [
        {
            author: 'Marcin',
            content: 'Dolor sit amet',
            title: 'Lorem Ipsum',
        }
    ];

    constructor() {
        this.initalizeRoutes();
    }

    public initalizeRoutes() {
        this.router.get(this.path, this.getAllPosts);
        this.router.post(this.path, this.createAPost);
    }

    private validatePost(body: unknown) {
        return this.postSchema.safeParse(body);
    }

    getAllPosts = (req: express.Request, res: express.Response) => {
        res.send(this.posts);
    };

    createAPost = (req: express.Request, res: express.Response) => {
        const post = this.validatePost(req.body);
        if (post.success) {
            this.posts.push(post.data);
            res.send(post.data);
        } else {
            res.status(405).send(post.error);
        }
    };
}

const middlewares = {
    logger: (req: Request, _res: Response, next: NextFunction) => { console.log(`${req.method} ${req.path}`); next(); },
    bodyParser: express.json()
} as const;

class App {
    public app: express.Application;
    public config: typeof config;

    constructor(controllers: Controller[], middleware?: typeof middlewares) {
        this.app = express();
        this.config = config;
        this.initializeMiddlewares();
        this.initializeControllers(controllers);

    }

    private initializeMiddlewares() {
        this.app.use(middlewares.logger);
    }

    private initializeControllers(controllers: Controller[]) {
        controllers.forEach(c => {
            this.app.use(middlewares.bodyParser);
            this.app.use(middlewares.logger);
            this.app.use('/', c.router);
        });
    }

    public listen() {
        this.app.listen(this.config.portListen, () => { console.log(`App started on port ${this.config.portListen}`); });
    }
}

const app = new App([
    new IndexController(),
    new PostsController(),
], middlewares);

app.listen();