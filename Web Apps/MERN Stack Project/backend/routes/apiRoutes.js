import express from 'express'
import { delProducts, getProducts, postProducts, putProducts } from '../controllers/productController.js';

const router = express.Router()

router.get("/", getProducts)

router.post("/", postProducts)

router.put("/:id", putProducts)

router.delete("/:id", delProducts)

export default router