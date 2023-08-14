import jwt from "jsonwebtoken";
import express from "express";
import type { Request, Response, NextFunction } from "express";
import bcrypt from "bcrypt";


function loggerMiddleware(req: Request, response: Response, next: NextFunction) {
    console.log(`${req.method} ${req.path}`);
    next();
}

const app = express();
app.use(loggerMiddleware);

app.get("/", (req, res) => {
    res.send("hello\n");
});

app.listen(5000);