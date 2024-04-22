## Log Analysis and Monitoring Tool

#### Overview
This tool comprises two components: a Bash script (log-monitor.sh) for real-time log monitoring and a Python script (log_analyzer.py) for analyzing log files and generating reports.

#### Bash Script (log_monitor.sh)
- The Bash script monitors a specified log file continuously using `tail -f` command. It displays new lines appended to the log file in real-time and gracefully handles interruptions such as `Ctrl+C`.

#### Python Script (log_analyzer.py)
- The Python script analyzes log files to extract `IP addresses`, `counts successful` and `failed attempts`, and generates a report in `CSV` format. It utilizes regular expressions for pattern matching and pandas for data manipulation.

#### Bash Script Usage 
1. Clone or download the `log-monitor.sh` script to your local machine.
2. Make the script executable: `chmod +x log_monitor.sh`
3. Run the script with the log file path as an argument: `./log_monitor.sh /path/to/log/file.log`
- location of the log file `/var/log` in linux 
- To redirect the output `> filename.txt or filename.log` after `./log_monitor.sh /path/to/log/file.log`

#### Python Script Usage
1. Ensure you have Python installed on your system.
2. Clone or download the `log_analyzer.py` script to your local machine.
3. Python libraries: `re, pandas, pprint`.
4. Run the script:
`python log_analyzer.py`
5. The script will read the serverlogs.log file by default and generate a report (output.csv) in the current directory. we can use any other generated logs and customize the regex accordingly to get the desire output. 

