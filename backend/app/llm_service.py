from __future__ import annotations

import os
from typing import Dict, Optional

import requests


class LLMService:
    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.provider = os.getenv("LLM_PROVIDER", "mock")

    def generate(self, context: str, question: str) -> str:
        if self.provider == "openai" and self.api_key:
            try:
                response = requests.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": "gpt-4o-mini",
                        "messages": [
                            {"role": "system", "content": "You are a helpful college student support assistant."},
                            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"},
                        ],
                    },
                    timeout=15,
                )
                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"]
            except Exception:
                pass

        return (
            f"AI response using local retrieval: {context[:250]}"
            if context
            else "I can help answer attendance, result, fee, timetable, assignment, notices, and academic policy questions."
        )


LLM_SERVICE = LLMService()
