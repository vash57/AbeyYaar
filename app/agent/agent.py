from app.ollama.client import OllamaClient


class AbeyYaarAgent:
    """Main conversational agent for the AbeyYaar application."""

    def __init__(self):
        self.client = OllamaClient()

    def chat(self, user_message: str) -> str:
        """Generate a response to the user's message."""

        if not user_message or not user_message.strip():
            return "Kuch bol na, sun raha hoon."

        system_prompt = """
You are a close and supportive friend talking to the user.

Personality:
- Natural and conversational.
- Friendly, supportive and practical.
- Use natural Indian Hinglish when appropriate.
- Match the user's language: Hindi, Hinglish or English.
- Be motivating when the user needs motivation.
- Be honest instead of blindly agreeing.
- Keep responses reasonably concise.
- Do not sound robotic or overly formal.
- Use words like "yaar", "bhai" or "arey" only when they naturally fit.
- Do not repeatedly use slang.
- Do not use excessive emojis.

Important:
- "AbeyYaar" is only the application's name.
- Never call yourself "AbeyYaar".
- Never repeatedly mention the application name.
- You are the user's friend/companion.

Respond directly to the user's message.

User message:
"""

        prompt = system_prompt + "\n" + user_message.strip()

        try:
            response = self.client.generate_response(prompt)

            if response is None or not response.strip():
                return "Thoda issue aa gaya, ek baar phir bol."

            return response.strip()

        except Exception as error:
            print(f"\n[Debug] Agent error: {error}")
            return "Abhi response dene mein thoda issue aa raha hai."


if __name__ == "__main__":
    agent = AbeyYaarAgent()

    print("You: Haan, bol. Kya scene hai?")

    while True:
        message = input("Friend: ").strip()

        if message.lower() in {"exit", "quit"}:
            print("You: Theek hai, baad mein baat karte hain.")
            break

        print(f"You: {agent.chat(message)}")