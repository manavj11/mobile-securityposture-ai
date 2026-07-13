"""
Local LLM client.

The LLM is only responsible for explaining findings and suggesting
security improvements.

It never determines the device risk level.
"""

import json
import requests


# Works with Ollama (OpenAI-compatible mode) or LM Studio.
API_URL = "http://localhost:11434/v1/chat/completions"

MODEL = "llama3.2"


SYSTEM_PROMPT = """
You are a mobile security expert.

You will receive:

1. Mobile device information
2. Risk level assigned by an Isolation Forest model

The risk assessment has already been completed.

Your responsibilities are ONLY:

- Briefly explain the findings.
- Recommend practical security improvements.
- Keep the response under 150 words.

If the risk is Critical,
reply exactly:

Manual review required.

Do not provide recommendations.
""".strip()


def get_recommendation(device: dict, risk: str) -> str:
    """
    Query the local LLM for security recommendations.
    """

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": json.dumps(
                    {
                        "risk": risk,
                        "device": device,
                    },
                    indent=2,
                ),
            },
        ],
        "temperature": 0.3,
    }

    response = requests.post(API_URL, json=payload, timeout=30)

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"].strip()