import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

CLAUDE_KEY = os.getenv("CLAUDE_KEY")

class ClaudeService:
    def __init__(self):
        if not CLAUDE_KEY:
            raise ValueError("CLAUDE_KEY is not set in the environment variables.")
        self.client = Anthropic(api_key=CLAUDE_KEY)

    def generate_response(self, prompt, max_tokens=1024):
        # TODO: Revert back to budget use
        formatted_prompt = (
            f"These logs are the result of an error when publishing some R or Python app."
            f" Please analyze the logs and provide a summary of the error.\n\n"
            f"Logs: '{prompt}'"
        )

        with self.client.messages.stream(
            model="claude-3-7-sonnet-20250219",
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": formatted_prompt}
            ],
        ) as stream:
            for text in stream.text_stream:
                yield text
