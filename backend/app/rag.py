from __future__ import annotations

from typing import Dict, List

from .data import KNOWLEDGE_BASE


class SimpleRAG:
    def __init__(self, knowledge: Dict[str, str]) -> None:
        self.knowledge = knowledge

    def search(self, question: str) -> str:
        normalized = question.lower()
        best_match = None
        best_score = -1

        for key, value in self.knowledge.items():
            score = sum(1 for term in key.replace("_", " ").split() if term in normalized)
            if score > best_score:
                best_score = score
                best_match = value

        return best_match or (
            "The college support assistant can answer questions about attendance, results, fees, timetable, assignments, notices, hostel, faculty, placement, library, events, and holidays."
        )


RAG_ENGINE = SimpleRAG(KNOWLEDGE_BASE)
