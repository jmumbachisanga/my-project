from src.ai_business_assistant.assistant import BusinessAssistant


def test_analyze_returns_structured_request() -> None:
    result = BusinessAssistant().analyze("How should I improve my customer retention?")

    assert result["status"] == "ready_for_ai_provider"
    assert result["challenge"] == "How should I improve my customer retention?"
    assert "Recommended next actions" in result["sections"]


def test_analyze_rejects_empty_challenge() -> None:
    try:
        BusinessAssistant().analyze("   ")
    except ValueError as exc:
        assert str(exc) == "Business challenge cannot be empty."
    else:
        raise AssertionError("Expected ValueError for an empty challenge")
