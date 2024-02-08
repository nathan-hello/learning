import { logger } from "./config";
import type { Request, Response, NextFunction } from "express";
import express from "express";
import { z } from "zod";




class HttpException extends Error {
    status: number;
    message: string;

    constructor(status: number, message: string) {
        super(message);
        this.status = status;
        this.message = message;
    }
}

export class WrongCredentialsException extends HttpException {
    constructor() {
        super(401, "Bad credentials");
    }
}

export class BadRegistryInfo extends HttpException {
    constructor() {
        super(401, "Bad registration details, or account already exists.");
    }
}

export class BadId extends HttpException {
    constructor() {
        super(404, "Bad post id");
    }
}

export class BadBody extends HttpException {
    constructor(error: string) {
        super(400, `Error when parsing body: ${error}`);
    }
}

function logging(req: Request, _res: Response, next: NextFunction) {
    logger.log("info", `REQUEST FROM IP: [${req.ip}] METHOD: [${req.method}] PATH: [${req.path}]`); next();
}

function bodyValidation(validator: z.AnyZodObject): express.RequestHandler {
    return (req, res, next) => {
        const v = validator.safeParse(req.body);
        if (!v.success) {
            next(new HttpException(400, v.error.toString()));
        } else {
            next();
        }
    };
}

function urlValidation(validator: z.ZodType<string | number> = z.string()): express.RequestHandler {
    return (req, res, next) => {
        const v = validator.safeParse(req.params);
        if (!v.success) {
            next(new HttpException(404, v.error.toString()));
        } else {
            next();
        }
    };
}

export const middlewares = {
    logging: logging,
    bodyValidation: bodyValidation,
    urlValidation: urlValidation
};
