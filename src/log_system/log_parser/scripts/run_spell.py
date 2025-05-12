#!/usr/bin/env python
# filepath: /home/u22/person/log-system/src/log_system/log_parser/scripts/run_spell.py
import os
import sys
from pathlib import Path
from log_system.config import Config
from log_system.log_parser.spell import LogParser

# Add the src directory to the Python path
src_path = Path(__file__).parents[4]
sys.path.insert(0, str(src_path))

def main():
    """
    Run the SPELL log parser on the specified log file.
    """
    # Setup paths and parameters
    input_dir = str(Config.DATA_PATH)  # Input directory containing log files
    output_dir = str(Config.DATA_PATH / "spell_results")  # Output directory for results
    log_file = "HDFS_2k.log"  # The log file to parse
    
    # HDFS log format
    log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'
    
    # Message type threshold (default: 0.5)
    tau = 0.5
    
    # Regular expression list for optional preprocessing (default: [])
    # You can add regex patterns to filter out parts of log messages
    regex = []
    
    # Create the parser instance
    parser = LogParser(
        indir=input_dir,
        outdir=output_dir,
        log_format=log_format,
        tau=tau,
        rex=regex
    )
    
    # Parse the log file
    print(f"Starting to parse log file: {log_file}")
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    
    # Check if log file exists
    log_file_path = os.path.join(input_dir, log_file)
    if not os.path.exists(log_file_path):
        print(f"Error: Log file not found: {log_file_path}")
        print("Please download the log file first using the download_logs.py script")
        return
    
    # Run the parser
    parser.parse(log_file)
    
    print(f"Parsing completed. Results saved to: {output_dir}")
    print(f"Structured logs: {output_dir}/{log_file}_structured.csv")
    print(f"Event templates: {output_dir}/{log_file}_templates.csv")

if __name__ == "__main__":
    main()