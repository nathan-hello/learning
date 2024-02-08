import { transports, createLogger, format } from "winston";
const { combine, timestamp, label, prettyPrint } = format;

export const logger = createLogger({
    transports: [
        new transports.File({
            dirname: "logs",
            filename: "node.log"
        })
    ],
    format: combine(
        timestamp(),
        prettyPrint()
    ),
});


export const config = {

    corsEnable: false,
    portListen: 3000
};