# Translator API with Groq Cloud LLaMA 3.3 70B

A **FastAPI-based Translator API** powered by **Groq Cloud LLaMA 3.3 70B** for high-quality translations. This API allows translating text from one language to another with a simple request.  

Designed with a **modular folder structure** for maintainability and scalability.

---

## Features

- Translate text between multiple languages using **LLaMA 3.3 70B**
- Clean architecture with separate folders for:
  - `routes/` – API endpoints
  - `services/` – Translation logic
  - `models/` – Pydantic models for request/response validation
  - `core/` – Configuration and utilities
- Input: `text` and `target_language`
- Output: `translated_text`
- Dockerfile included for containerized deployment
- Hot-reload support during development

---

## Installation

Clone the repository and set up a virtual environment:

```bash
git clone <your-repo-url>
cd translator-api
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
````

---

## Running the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Access the API at:

```
http://127.0.0.1:8000
```

Example POST request:

```json
POST /translate
{
  "text": "Hello how are you",
  "target_language": "Urdu"
}
```

Response:

```json
{
  "translated_text": "ہیلو آپ کیسے ہیں"
}
```

---

## Project Structure

```text
translator-api/
│
├─ app/
│   ├─ main.py                  # FastAPI app
│   ├─ core/
│   │   └─ config.py            # API keys, config
│   ├─ models/
│   │   └─ translation_model.py # Request/response Pydantic models
│   ├─ routes/
│   │   └─ translation_routes.py # API endpoints
│   └─ services/
│       └─ translation_service.py # Translation logic using Groq Cloud LLaMA
├─ requirements.txt
├─ Dockerfile
└─ .gitignore
```

---

## Dependencies

* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* Groq Cloud SDK
* Python 3.10+

---

## Docker Usage

Build and run the container:

```bash
docker build -t translator-api .
docker run -p 7860:7860 translator-api
```

---
