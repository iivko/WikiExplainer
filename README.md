# 🧠 WikiExplainer

**WikiExplainer** is my first experiment building a LangChain-powered agent that uses tools like Tavily Search and the Wikipedia API to generate smart explanations of any topic you enter.

> ⚠️ All functions and logic are in prototype state — the goal was to explore LangChain and langchain-ollama capabilities.

---

## 🖼️ Frontend

Built with **React + TailwindCSS**, the frontend provides a clean and user-friendly interface:

![WikiExplainer UI](./images/screenshot.png)

---

## 📺 Demo Video

Watch the app in action here:

[![Watch the demo](https://img.youtube.com/vi/LFBhi5BZuz0/hqdefault.jpg)](https://youtu.be/LFBhi5BZuz0)

---

## 🧠 How it Works

1. You enter a topic (e.g. *Electron*, *Black Holes*, *Sofia*).
2. The backend agent (via LangChain) uses a **Tavily AI search tool** to find the relevant topic URL.
3. Then it connects directly to the **Wikipedia API** to fetch rich data.
4. The AI:
   - Generates an explanation in simple terms
   - Lists 3 fun or surprising facts
   - Finds and returns a related image

All powered by `langchain`, `langchain_community`, and `langchain_ollama` locally.

---

## 🔧 Stack

- **Frontend**: React + Vite + TailwindCSS
- **Backend**: Django + Django REST Framework
- **AI/Agent**: LangChain + Ollama (locally) + Tavily API + Wikipedia
