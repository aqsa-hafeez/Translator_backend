from fastapi import APIRouter
from app.models.translation_model import TranslationRequest, TranslationResponse
from app.services.translation_service import translate_text

router = APIRouter()

@router.post("/translate", response_model=TranslationResponse)
def translate(data: TranslationRequest):

    result = translate_text(
        text=data.text,
        target_language=data.target_language
    )

    return TranslationResponse(translated_text=result)