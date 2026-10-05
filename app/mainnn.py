from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from app.agent.agent import AbeyYaarAgent


agent = AbeyYaarAgent()


class ChatHandler(BaseHTTPRequestHandler):

    def _send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "http://localhost:5173")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
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
                self._send_json({"error": "Message is required"}, 400)
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


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), ChatHandler)

    print("=============================================")
    print("        AbeyYaar Backend API")
    print("=============================================")
    print("API: http://127.0.0.1:8000")
    print("Chat: POST /api/chat")
    print("Press Ctrl+C to stop.")

    server.serve_forever()