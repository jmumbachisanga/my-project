"""Application configuration.

Secrets are read from environment variables and are never hard-coded.
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the assistant."""

    ai_api_key: str | None = os.getenv("AI_API_KEY")
    ai_model: str = os.getenv("AI_MODEL", "default")
