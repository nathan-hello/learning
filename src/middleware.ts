import { logger } from "./config";
import type { Request, Response, NextFunction } from "express";
import express from "express";

export function log(req: Request, _res: Response, next: NextFunction) {
    logger.log("info", `REQUEST FROM IP: [${req.ip}] METHOD: [${req.method}] PATH: [${req.path}]`); next();
}


class HttpException extends Error {
    status: number;
    message: string;

    constructor(status: number, message: string) {
        super(message);
        this.status = status;
        this.message = message;
    }
}



export function validate(data: unknown)


