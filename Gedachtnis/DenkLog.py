# Module to log messages with a timestamp.

import datetime
import os

def log_message(message):
    """
    Appends a message with a timestamp to the DenkLog.txt file.

    Args:
        message (str): The message to be logged.
    """
    # IMPORTANT: Rename 'Gedachtnis' to 'Gedächtnis' in your environment.
    log_file_path = os.path.join('Gedachtnis', 'DenkLog.txt')

    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the log entry
    log_entry = f"[{timestamp}] {message}\n"

    # Append the log entry to the file
    with open(log_file_path, 'a', encoding='utf-8') as f:
        f.write(log_entry)

# Example usage (for testing purposes)
if __name__ == '__main__':
    log_message("This is a test log entry.")
    log_message("This is another test log entry.")
    print("Log entries have been written to DenkLog.txt.")
