#!/bin/bash
# Get the log file path as an argument
log_file="$1"

# Check if a file path is provided
if [ -z "$log_file" ]; 
then
echo "Please provide a log file path as an argument."
exit 1
fi

# Trap the Ctrl+C signal to exit.
trap "echo; exit 0" SIGINT

# Continuously monitor the log file with tail -f
tail -f "$log_file"
