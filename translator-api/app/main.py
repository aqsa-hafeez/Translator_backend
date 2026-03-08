from fastapi import FastAPI
from app.routes.translation_routes import router as translation_router

app = FastAPI(title="Groq LLaMA Translation API")

app.include_router(translation_router)




