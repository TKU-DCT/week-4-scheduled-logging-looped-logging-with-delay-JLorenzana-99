import psutil
from datetime import datetime
import csv
import os
import time

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Use psutil to get CPU, memory, and disk usage
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    return [now, cpu, memory, disk]

def write_log(data):
    # Check if log.csv exists
    file_exists = os.path.isfile('log.csv')
    
    # Open file in append mode
    with open('log.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # If file doesn't exist, write header row first
        if not file_exists:
            writer.writerow(['Timestamp', 'CPU', 'Memory', 'Disk'])
        
        # Append the current data row
        writer.writerow(data)

if __name__ == "__main__":
    # Loop 5 times to collect 5 log entries
    for i in range(5):
        row = get_system_info()
        write_log(row)
        print(f"Logged entry {i+1}/5:", row)
        
        # Wait 10 seconds before next entry (except after the last one)
        if i < 4:
            time.sleep(10)
    
    print("\nLogging complete! 5 entries added to log.csv")