import csv
import os
import time

while True:
    try:
        # Get the current directory
        current_dir = os.getcwd()
        # Construct the full file path for the log file
        log_file_path = os.path.join(current_dir, "idea2.log")
        # Open the log file in "tail" mode (to read the latest lines)
        with open(log_file_path, "r", encoding="utf-8") as logfile:
            logfile.seek(0,2)  # Go to the end of the file
            line = logfile.readlines()[-1]  # get the last line which is the latest recorded in the logfile.
            if line.startswith("CurrentLocation"):  # Check if the line starts with "CurrentLocation"
                # Copy the whole line to the CSV
                with open("output.csv", "a", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([line])
            time.sleep(1)  # Wait 1 second before checking the next line
    except FileNotFoundError:
        print("Error: Logfile not found in the current directory")
    except PermissionError:
        print("Error: Permission denied to access the logfile")
    except Exception as e:
        print("Error: ", e)
        time.sleep(1)