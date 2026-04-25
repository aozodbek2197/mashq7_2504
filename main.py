import json
from typing import Any, Dict

class JSONProcessor:
    def __init__(self, json_string: str) -> None:
        self.json_string = json_string
        self.data: Dict[str, Any] = {}

    def parse(self) -> None:
        try:
            self.data = json.loads(self.json_string)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            self.data = {}

    def get_value(self, key: str) -> Any:
        return self.data.get(key, None)


if __name__ == "__main__":
    raw = '{"name": "Ali", "age": 25}'
    processor = JSONProcessor(raw)
    processor.parse()
    print(processor.get_value("name"))
