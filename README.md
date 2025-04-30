
# 🪨 What Beats Rock? — GenAI Guessing Game 🎮

A fun and intelligent word game where users guess what metaphorically "beats" the previous word — powered by Google Gemini Pro!

Built for the Wasserstoff Gen-AI Internship Task.

---

## 🧠 Overview

- Start with a seed word: `"Rock"`
- Player makes creative guesses
- A Gemini-powered AI decides if the new word *beats* the previous one
- Score increases with valid guesses
- Duplicate guesses end the game
- Inappropriate words are blocked
- Caching, personas, and global stats included!

---

## ✅ Features Implemented

| Feature | Status |
|--------|--------|
| Gen-AI prompt handling via Gemini Pro | ✅ |
| AI verdict: YES/NO using short prompts | ✅ |
| Score + guess tracking with linked list | ✅ |
| Redis-based caching | ✅ |
| Global per-word guess counter in PostgreSQL | ✅ |
| Profanity moderation | ✅ |
| Persona toggle (cheery / serious) | ✅ |
| Hosted frontend (HTML + CSS + JS) served via FastAPI | ✅ |

---

## 🚀 Getting Started (Docker Setup)

### 1. Clone this repo

```bash
git clone https://github.com/your-username/genai-guessing-game.git
cd genai-guessing-game
```

### 2. Add `.env` file

Create a `.env` file in the root:

```
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=postgresql://user:pass@db:5432/game
REDIS_HOST=redis
```

### 3. Build & Start with Docker

```bash
docker compose up --build
```

Then open [http://localhost:8000](http://localhost:8000)

> Your FastAPI backend + PostgreSQL + Redis + Frontend will run in one command.

---

## 🖥️ Frontend Features

- Persona selector (`cheery`, `serious`)
- Input field for guess
- Emoji-rich feedback
- Last 5 guesses tracker
- Score counter
- Global guess count shown in messages

---

## 📦 API Routes

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/guess` | POST | Submit a guess (`{ "guess": "Paper" }`) |
| `/history` | GET | Returns guess history + score |
| `/reset` | GET | Resets the game |
| `/status` | GET | (Optional) Health check route |

---

## ⚠️ Notes

- Make sure your Gemini API key is valid and supports `models/gemini-pro`
- Redis is required for caching responses
- PostgreSQL stores global guess counters

---

## ✨ Screenshots

> *(Optional – add a screenshot of your app here)*

```
📸 ./frontend/screenshot.png
```

---

## 👨‍💻 Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [Google Gemini (generativeai)](https://ai.google.dev/)
- [PostgreSQL + SQLAlchemy](https://www.sqlalchemy.org/)
- [Redis](https://redis.io/)
- [Docker](https://www.docker.com/)
- [Vanilla HTML/CSS/JS](https://developer.mozilla.org/en-US/)

---

## 📬 Submission Checklist

- ✅ `README.md` (this file)
- ✅ Code runs with `docker compose up --build`
- ✅ Gemini API key passed via `.env`
- ✅ Game works with caching + global DB count
- ✅ Frontend accessible at `http://localhost:8000`

---

## 👏 Thanks!

Created with ❤️ for the Wasserstoff Gen-AI Internship.
