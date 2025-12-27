import psutil
# Check CPU Threshold Value
def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU threshold: "))
    current_cpu = psutil.cpu_percent(interval=1)
    print(f"Current CPU: {current_cpu}%")

    if current_cpu > cpu_threshold:
        print("CPU Alert Email sent..")
    else:
        print("CPU is in safe state")

# Check Disk Threshold Value
def check_disk_threshold():
    disk_threshold = int(input("Enter the disk threshold: "))
    current_disk = psutil.disk_usage('C:\\').percent
    print(f"Current Disk: {current_disk}%")

    if current_disk > disk_threshold:
        print("Disk Alert! Email sent..")
    else:
        print("Disk is in safe state")

# Check Memory Threshold Value

def check_memory_threshold():
    memory_threshold = int(input("Enter the Memory threshold: "))
    current_memory = psutil.virtual_memory().percent
    print(f"current_memory: {current_memory}%")

    if current_memory > memory_threshold:
        print("Memory Alert! Email sent")
    else:
        print("Memory is in safe state")

# Main function to check all thresholds
def monitor_system():
    print("=== System Monitoring ===")
    
    check_cpu_threshold()
    
    check_disk_threshold()
    
    check_memory_threshold()

# Run the monitoring
monitor_system()


