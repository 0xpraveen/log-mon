import re  # Importing the regular expression module
import pandas as pd  # Importing pandas for data manipulation
import pprint  # Importing pprint for pretty printing
logfile = open("serverlogs.log", "r")  # Opening the log file in read mode

# Regular expression pattern to match IP addresses
pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

ip_addrs_lst = []  # List to store IP addresses
failed_lst = []  # List to store failed attempts
success_lst = []  # List to store successful attempts

# Iterating through each log entry in the logfile
for log in logfile:
    ip_add = re.search(pattern, log)  # Searching for IP addresses in the log entry
    ip_addrs_lst.append(ip_add.group())  # Appending the found IP address to the list
    lst = log.split(" ")  # Splitting the log entry by space
    failed_lst.append(int(lst[-1]))  # Appending the last element (failed attempts) to the failed list
    success_lst.append(int(lst[-4]))  # Appending the fourth last element (successful attempts) to the success list

# Calculating total failed and successful attempts
total_failed = sum(failed_lst)
total_success = sum(success_lst)

# Appending total counts to respective lists
ip_addrs_lst.append("Total")
success_lst.append(total_success)
failed_lst.append(total_failed)

# Creating a DataFrame to store IP addresses, successful attempts, and failed attempts
df = pd.DataFrame(columns=['IP Address', "Success", "Failed"])
df['IP Address'] = ip_addrs_lst
df["Success"] = success_lst
df["Failed"] = failed_lst

# Writing the DataFrame to a CSV file
df.to_csv("output.csv", index=False)

# Pretty printing the DataFrame
pprint.pprint(df)
