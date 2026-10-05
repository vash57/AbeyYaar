import os
import requests
from typing import Optional


class OllamaClient:
    """Client for interacting with a local Ollama server."""

    def __init__(self):
        self.base_url = os.getenv(
            "OLLAMA_BASE_URL",
            "http://localhost:11434"
        )
        self.model = os.getenv(
            "OLLAMA_MODEL",
            "gemma4:e2b"
        )

    def generate_response(
        self,
        prompt: str,
        temperature: float = 0.7
    ) -> Optional[str]:

        url = f"{self.base_url}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature
            }
        }

        try:
            response = requests.post(
                url,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            result = response.json()
            return result.get("response")

        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to Ollama.")
            return None

        except requests.exceptions.Timeout:
            print("Error: Ollama request timed out.")
            return None

        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Ollama: {e}")
            return None
