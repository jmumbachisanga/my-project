# AI Architecture

## Purpose

The AI layer converts a user's business challenge into a structured analysis while keeping business logic separate from the external AI provider.

## Flow

```text
User business challenge
        ↓
Input validation
        ↓
Prompt builder
        ↓
AI client interface
        ↓
AI provider implementation
        ↓
Structured business guidance
```

## Design principles

- Provider-independent core logic
- No API keys in source code
- Testable without network access
- Clear separation between prompts and application logic
- Human-readable, actionable outputs

## Next implementation

The next step is to add an OpenAI provider adapter behind the `AIClient` interface. Credentials must be supplied through environment configuration and never committed to GitHub.
