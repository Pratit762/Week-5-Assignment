import time

class MetricsCollector:
    def __init__(self):
        self.metrics = {"items_checked": 0, "issues_detected": 0}

    def log_item_checked(self):
        self.metrics["items_checked"] += 1

    def log_issue_detected(self):
        self.metrics["issues_detected"] += 1

    def snapshot(self):
        return {**self.metrics, "timestamp": time.time()}
