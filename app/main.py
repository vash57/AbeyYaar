from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import threading

from app.agent.agent import AbeyYaarAgent


agent = AbeyYaarAgent()


class ChatHandler(BaseHTTPRequestHandler):

    def _send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )
        self.send_header(
            "Access-Control-Allow-Origin",
            "http://localhost:5173"
        )
        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type"
        )
        self.send_header(
            "Access-Control-Allow-Methods",
            "POST, OPTIONS"
        )
        self.end_headers()

        self.wfile.write(body)

    def do_OPTIONS(self):
        self._send_json({"ok": True})

    def do_POST(self):
        if self.path != "/api/chat":
            self._send_json({"error": "Not found"}, 404)
            return

        try:
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length))

            message = data.get("message", "").strip()

            if not message:
                self._send_json(
                    {"error": "Message is required"},
                    400
                )
                return

            response = agent.chat(message)

            self._send_json({
                "response": response
            })

        except Exception as error:
            print(f"[API Error] {error}")

            self._send_json({
                "error": "Something went wrong."
            }, 500)

    def log_message(self, format, *args):
        # Terminal ko HTTP logs se clean rakho
        pass


def start_server():
    server = HTTPServer(
        ("127.0.0.1", 8000),
        ChatHandler
    )

    server.serve_forever()


def terminal_chat():

    print()
    print("==============================")
    print("        Your AI Friend")
    print("==============================")
    print("Type 'exit' to quit.")
    print()

    while True:

        try:
            message = input("You: ").strip()

            if not message:
                continue

            if message.lower() == "exit":
                print("\nFriend: Chal bhai, milte hain!")
                break

            print("\nFriend: Thinking...", end="\r", flush=True)

            response = agent.chat(message)

            # Thinking line ko overwrite karke actual response
            print(" " * 40, end="\r")

            print(f"Friend: {response}")
            print()

        except KeyboardInterrupt:
            print("\n\nFriend: Chal bhai, milte hain!")
            break

        except Exception as error:
            print(f"\nFriend: Sorry bhai, error aa gaya: {error}\n")


if __name__ == "__main__":

    # API background me start
    server_thread = threading.Thread(
        target=start_server,
        daemon=True
    )

    server_thread.start()

    # Terminal conversation
    terminal_chat()