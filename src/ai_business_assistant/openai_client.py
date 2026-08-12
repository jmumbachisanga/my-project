from __future__ import annotations

from typing import Protocol

from .prompts import BUSINESS_ANALYSIS_PROMPT, SYSTEM_PROMPT


class AIClient(Protocol):
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        ...


def build_business_analysis_prompt(challenge: str) -> str:
    if not challenge or not challenge.strip():
        raise ValueError("Business challenge cannot be empty.")
    return BUSINESS_ANALYSIS_PROMPT.format(challenge=challenge.strip())


def analyze_business_challenge(client: AIClient, challenge: str) -> str:
    """Send a validated business challenge to an injected AI client.

    The client is injected so the core application can be tested without
    requiring an API key or a live network request.
    """
    prompt = build_business_analysis_prompt(challenge)
    return client.generate(SYSTEM_PROMPT, prompt)
