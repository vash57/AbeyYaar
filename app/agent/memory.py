import json
from pathlib import Path


class Memory:
    """Simple local JSON-based memory."""

    def __init__(self, file_path="data/student_profile.json"):
        self.file_path = Path(file_path)
        self._ensure_file()
        self.data = self._load()

    def _ensure_file(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            self.file_path.write_text(
                json.dumps({}, indent=4),
                encoding="utf-8"
            )

    def _load(self):
        try:
            return json.loads(
                self.file_path.read_text(encoding="utf-8")
            )
        except (json.JSONDecodeError, OSError):
            return {}

    def save(self):
        self.file_path.write_text(
            json.dumps(
                self.data,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def get(self, key, default=None):
        return self.data.get(key, default)

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save()

    def all(self):
        return self.data.copy()