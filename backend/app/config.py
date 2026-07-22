from __future__ import annotations

import os


class Settings:
    llm_provider: str = os.getenv("LLM_PROVIDER", "mock")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    use_ml_classifier: bool = os.getenv("USE_ML_CLASSIFIER", "true").lower() == "true"


SETTINGS = Settings()
