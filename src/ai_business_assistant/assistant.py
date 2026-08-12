"""Core business-assistant service.

This module intentionally contains a provider-independent MVP boundary.
AI provider integration will be added in a later implementation step.
"""


class BusinessAssistant:
    """Prepare a business challenge for structured AI analysis."""

    def analyze(self, challenge: str) -> dict[str, object]:
        """Return a validated analysis request structure.

        The current implementation is deliberately provider-independent so the
        application can be tested before an external AI service is connected.
        """
        cleaned = challenge.strip()
        if not cleaned:
            raise ValueError("Business challenge cannot be empty.")

        return {
            "challenge": cleaned,
            "sections": [
                "Situation",
                "Key considerations",
                "Recommended next actions",
            ],
            "status": "ready_for_ai_provider",
        }
