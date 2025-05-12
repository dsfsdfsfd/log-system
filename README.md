# Log Analysis System

A log analysis system with integrated anomaly detection features.

## Project Structure

```
log-system/
├── src/
│   └── log_system/            # Main source code
│       ├── config.py          # System configuration
│       ├── log_parser/        # Log parsing module
│       │   ├── spell.py       # SPELL algorithm
│       │   └── scripts/       # Analysis scripts
│       │       ├── download_logs.py
│       │       └── run_spell.py
│       └── anomaly_detection/ # Anomaly detection module
└── .env                       # Environment variables configuration
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/username/log-system.git
cd log-system
```

2. Create a virtual environment and install dependencies using uv:
```bash
uv venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
uv pip install -e .
```

3. Configure the `.env` file:

## Usage

1. Download the log file:
```bash
uv run python src/log_system/log_parser/scripts/dowload_logs.py
```

2. Run the SPELL analysis:
```bash
uv run python src/log_system/log_parser/scripts/run_spell.py
```

## References

- [SPELL: Streaming Parser for Event Logs using LCS](https://github.com/logpai/logparser)
- [LogHub: A Large Collection of System Log Datasets](https://github.com/logpai/loghub)
