import json
import random
from datetime import datetime

def generate_log_entry():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "event": random.choice(["checked", "low_stock", "restocked"]),
        "item": random.choice(["item001", "item002", "item003"]),
        "quantity": random.randint(0, 15)
    }

def generate_logs(n=20):
    return [generate_log_entry() for _ in range(n)]

if __name__ == "__main__":
    logs = generate_logs()
    with open("data/fake_logs.json", "w") as f:
        json.dump(logs, f, indent=4)
