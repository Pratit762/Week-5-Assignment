class InventoryBot:
    def __init__(self, logger, metrics):
        self.logger = logger
        self.metrics = metrics
        self.inventory = {
            'item001': 10,
            'item002': 0,
            'item003': 3
        }

    def check_inventory(self):
        for item_id, qty in self.inventory.items():
            self.logger.info(f"Checking {item_id} with quantity: {qty}")
            self.metrics.log_item_checked()

            if qty <= 2:
                self.logger.warning(f"Low stock alert for {item_id}")
                self.metrics.log_issue_detected()
