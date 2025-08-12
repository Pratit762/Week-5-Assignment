import json
from pathlib import Path
import time

log_path = Path(__file__).parent / "data" / "fake_logs.json"

# Load the existing log
with open(log_path, "r") as f:
    log_data = json.load(f)

# Update the log
log_data["timestamp"] = time.time()

with open(log_path, "w") as f:
    json.dump(log_data, f, indent=4)

# Print confirmation
print("Log updated:", log_data)
