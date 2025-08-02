// Entry point of API
import express from 'express';
import dotenv from 'dotenv';
import { connectDB } from './config/db.js'
import apiRoutes from "./routes/apiRoutes.js"
import path from "path"
import { fileURLToPath } from 'url'

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

app.use(express.json()); // allows us to accept json

app.use("/api/products", apiRoutes)

if(process.env.NODE_ENV === "production") {
    const frontendPath = path.resolve(__dirname, "..", "frontend", "dist");
    console.log("NODE_ENV:", process.env.NODE_ENV);
    console.log("Serving static from:", frontendPath);

    app.use(express.static(frontendPath));

    app.get("*", (req, res) => {
        res.sendFile(path.resolve(frontendPath, "index.html"))
    })
}

app.listen(PORT, () => {
    connectDB();
    console.log(`Started at http://localhost:${PORT}`);
});