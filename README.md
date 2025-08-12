# Week-5-Assignment
The Inventory Bot Enterprise is a Python-based automation tool designed to monitor and manage inventory data across multiple warehouses, markets, or teams. Originally developed as a small pilot, this version has been upgraded for enterprise-wide rollout, with added features like monitoring, logging, and maintainability.

🚀 Features
Automated Inventory Checks – Scans for low-stock or missing items.

Monitoring & Logging – Stores log files in src/data/fake_logs.json.

Scalable Architecture – Designed for deployment across multiple warehouses.

Maintenance Plan – Documented steps for ensuring system reliability.

ROI Model – Estimates cost savings and efficiency improvements.

📂 Project Structure

inventory-bot-enterprise/
│
├── src/
│   ├── main.py               # Main entry point of the bot
│   ├── monitor.py            # Monitoring functions
│   ├── maintenance.py        # Maintenance-related utilities
│   ├── roi.py                # ROI calculation functions
│   └── data/
│       └── fake_logs.json    # Log file output
│
├── docs/
│   ├── monitoring_architecture.png  # Architecture diagram
│   ├── maintenance_plan.md          # Maintenance strategy document
│   └── roi.md                       # ROI model documentation
│
├── README.md                # Project description
└── requirements.txt         # Python dependencies
🛠 Installation & Setup
Clone the repository


git clone https://github.com/yourusername/inventory-bot-enterprise.git

cd inventory-bot-enterprise
Install dependencies


pip install -r requirements.txt
Run the bot


cd src
python main.py
📊 How It Works
The bot scans a set of predefined inventory data.

It checks for low stock or missing items.

It logs results in src/data/fake_logs.json.

Monitoring tools read the logs for visualization.

📄 Documentation
Maintenance Plan – Step-by-step guide for keeping the bot running smoothly.

ROI Model – Explains the return on investment for enterprise deployment.

Monitoring Architecture – Visual diagram of system monitoring.

👨‍💻 Author
Developed by Pratit Agnihotri for educational and demonstration purposes.
