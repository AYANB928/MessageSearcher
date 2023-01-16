import csv
import os

# Path to the chat history file
CHAT_HISTORY_FILE = '/path/ParseThisFile.txt'

# Open the chat history file
with open(CHAT_HISTORY_FILE, 'r', encoding='utf-8') as f:
    # Read the file line by line
    lines = f.readlines()[1:]

# Open a CSV file for writing
with open('/path/to/newFile.txt', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the column headers
    writer.writerow(['Timestamp', 'Sender', 'Message'])

    # Iterate over the lines 
    for line in lines:
        # Split the line into columns
        columns = line.split('-')
        if len(columns) >= 2:
            # Extract the timestamp, sender, and message
            timestamp = columns[0][0:]
            message = columns[1][1:]

            column_sender = message.split(':')
            if len(column_sender) >= 2:
                sender = column_sender[0][0:]
                sender_message = column_sender[1][1:]
                
                if 'type what you want searched' in sender_message.lower():
					
					#Write the message to the CSV file
                    writer.writerow([timestamp, sender, sender_message])

print('Done!')