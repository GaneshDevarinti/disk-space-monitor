import psutil
from datetime import datetime
# Settings - you can change this number
THRESHOLD = 80#Alert if disk is more than 80% full
def check_disk():
    # Get disk usage percentage
    disk = psutil.disk_usage('/').percent
    # Get current time
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Write to log file
    with open('disk_log.txt', 'a') as f:
        f.write(f"{timestamp} - Disk Usage: {disk}%\n")
    # Check if disk is too full
    if disk > THRESHOLD:
        alert_msg = f"WARNING: Disk at {disk}%!"
        print(alert_msg)
        # Write alert to separate file
        with open('alerts.txt', 'a') as f:
            f.write(f"{timestamp} - {alert_msg}\n")
    else:
        print(f"OK: Disk at {disk}%")
# Run the check
if __name__ == "__main__":
    check_disk()