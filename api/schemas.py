"""
Pydantic schemas for request/response models.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    version: str


class ModelsResponse(BaseModel):
    models: list[str]
    default: str


class TranscriptionResponse(BaseModel):
    text: str
    language: str
    engine: str
    model: str | None = None
    segments: list[dict[str, Any]] = []
    filename: str | None = None
