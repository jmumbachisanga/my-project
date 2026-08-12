import pytest

from ai_business_assistant.openai_client import (
    analyze_business_challenge,
    build_business_analysis_prompt,
)


class FakeAIClient:
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        assert "AI business assistant" in system_prompt
        assert "Improve customer retention" in user_prompt
        return "Test analysis"


def test_build_prompt_rejects_empty_challenge():
    with pytest.raises(ValueError):
        build_business_analysis_prompt("   ")


def test_analyze_business_challenge_uses_injected_client():
    result = analyze_business_challenge(FakeAIClient(), "Improve customer retention")
    assert result == "Test analysis"
