"""
Esquemas Pydantic para la validación de entradas y salidas del Chatbot de Voz ETITC.
VERSIÓN PLANTILLA PARA ESTUDIANTES.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class AudioConsultationRequest(BaseModel):
    """
    Solicitud de entrada al endpoint de voz.
    (Entregado como base para que los demás módulos conozcan la firma de entrada).
    """
    session_id: str = Field(default="sesion-aspirante-001")
    audio_id_simulado: Optional[str] = Field(default=None)
    audio_base64: Optional[str] = Field(default=None)
    texto_directo: Optional[str] = Field(default=None)
    incluir_saludo_inicial: bool = Field(default=False)


class STTResult(BaseModel):
    """Resultado estructurado del servicio Speech-to-Text (STT)."""
    texto_original: str
    texto_normalizado: str
    fuente_reconocimiento: str
    confianza_stt: float = Field(ge=0.0, le=1.0)


class IntentMatchResult(BaseModel):
    """Resultado del motor determinista de intenciones institucionales."""
    intent_id: str
    categoria: str
    puntaje_coincidencia: float = Field(ge=0.0, le=1.0)
    keywords_detectadas: List[str]
    respuesta_institucional_exacta: str
    enlaces_oficiales: List[str]
    es_fallback: bool


class TTSOutput(BaseModel):
    """Resultado del sintetizador de voz (TTS) con personalidad de estudiante ETITC."""
    guion_hablado_estudiante: str
    ssml_generado: str
    audio_wav_base64: str
    duracion_estimada_segundos: float
    perfil_voz: str


class VoiceChatResponse(BaseModel):
    """
    Respuesta integral del endpoint principal `/api/v1/chat/voz`.
    """
    session_id: str
    transcripcion: STTResult
    intencion: IntentMatchResult
    voz_estudiante: TTSOutput
    garantia_no_alucinacion: bool = True
