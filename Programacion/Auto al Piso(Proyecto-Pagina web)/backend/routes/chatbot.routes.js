import express from 'express';
import { responderChatbot } from '../controllers/chatbot.controller.js';

const router = express.Router();

router.post('/', responderChatbot);

export default router;
