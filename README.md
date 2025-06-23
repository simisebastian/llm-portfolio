# 🧠 SEQATO LLM Awareness Program – Portfolio Repository

This repository contains all the projects I’ve built as part of the **SEQATO LLM Awareness and Portfolio Development Program**. It showcases my learning journey through mini-projects, intermediate tools, and a final portfolio-level application using LLMs, FastAPI, Streamlit, and Hugging Face.

---

## 📅 Program Structure

| Phase      | Month | Focus Area                            | Deliverables                                |
|------------|--------|----------------------------------------|---------------------------------------------|
| Phase 1    | Month 1 | Foundations & Setup                    | Mini Projects (Chat App, Summarizer)        |
| Phase 2    | Month 2 | Intermediate Tools & Applications      | Topic Tracker, Multi-Modal, Audio Extractor |
| Phase 3    | Month 3 | Portfolio Project                      | Custom Chatbot / LangGraph / QLoRA          |

---

## ✅ Phase 1: Foundations & Mini Projects

> Goal: Understand LLM basics and build simple tools using Python

### 📂 [`phase-1/llm-chat-app`](./phase-1/llm-chat-app/)
- **Description**: A local chatbot interface built with Streamlit, FastAPI, and Ollama LLM.
- **Stack**: Python, Streamlit, FastAPI, Ollama
- **Skills Gained**: Prompting, state management, real-time chat interface

### 📂 [`phase-1/document-summarizer`](./phase-1/document-summarizer/)
- **Description**: A PDF uploader that summarizes documents using Hugging Face transformers.
- **Stack**: Python, Hugging Face, PyMuPDF
- **Skills Gained**: NLP summarization, file handling, pipeline usage

---

## 🛠️ Phase 2: Intermediate Projects

> Goal: Combine LLMs with other AI tools like Whisper and vision models

### 📂 [`phase-2/news-tracker`](./phase-2/news-tracker/)
- Scrapes Google News and summarizes trending topics using LLMs.

### 📂 [`phase-2/multimodal-assistant`](./phase-2/multimodal-assistant/)
- Answers queries based on images and text using OpenAI Vision or HF Vision transformers.

### 📂 [`phase-2/meeting-notes-extractor`](./phase-2/meeting-notes-extractor/)
- Converts meeting audio into structured notes and tasks using Whisper + GPT.

---

## 🚀 Phase 3: Final Portfolio Project

> Goal: Create a production-ready full project

### 📂 [`phase-3/final-project`](./phase-3/final-project/)
Choose one of:
- [ ] Custom Chatbot with RAG (LangChain + ChromaDB)
- [ ] Multi-Agent Dev Assistant using LangGraph
- [ ] Price Prediction Fine-Tuning using QLoRA

Includes:
- Problem Statement  
- Architecture Diagram  
- Code + UI  
- README + Demo (if applicable)  

---

## 🧠 Skills Learned

- Python + API Development (FastAPI)
- Web UI with Streamlit
- Prompt Engineering
- Whisper Speech-to-Text
- Hugging Face Transformers
- LLM Architecture: RAG, LangGraph, Fine-Tuning
- Git & GitHub Project Management

---

## 📎 How to Run Projects

Each project includes its own `README.md` and instructions.

Common install steps:

```bash
# Create virtual environment (optional)
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
