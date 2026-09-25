import os
import requests


def create_story(user_idea, language="English"):
    """
    Generate a structured kids cartoon story using an AI API.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    # Temporary fallback if API key is not connected yet
    if not api_key:
        return {
            "title": "My Kids Cartoon",
            "language": language,
            "idea": user_idea,
            "scenes": [
                {
                    "scene": 1,
                    "description": user_idea,
                    "dialogue": "",
                    "duration": 5
                }
            ]
        }

    prompt = f"""
Create a short, child-friendly cartoon story.

Story idea:
{user_idea}

Language:
{language}

Create 5 short scenes.

Return ONLY valid JSON in this format:

{{
  "title": "story title",
  "scenes": [
    {{
      "scene": 1,
      "description": "scene description",
      "dialogue": "spoken dialogue",
      "duration": 6
    }}
  ]
}}

Rules:
- Make it suitable for children.
- Keep the story positive and educational.
- Use simple language.
- Each scene should be visually interesting.
- No violence or frightening content.
"""

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7
        },
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    content = data["choices"][0]["message"]["content"]

    import json

    story = json.loads(content)

    story["language"] = language
    story["idea"] = user_idea

    return story
