import platform
import psutil
import subprocess

def print_system_info():
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")

def print_cpu_info():
    cpu_freq = psutil.cpu_freq()
    print(f"Max Frequency: {cpu_freq.max:.2f}Mhz")
    print(f"Min Frequency: {cpu_freq.min:.2f}Mhz")
    print(f"Current Frequency: {cpu_freq.current:.2f}Mhz")
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage Percentage: {cpu_percent}%")

def print_memory_info():
    svmem = psutil.virtual_memory()
    print(f"Total: {svmem.total / (1024 * 1024 * 1024)}Gb")
    print(f"Available: {svmem.available / (1024 * 1024 * 1024)}Gb")
    print(f"Used: {svmem.used / (1024 * 1024 * 1024)}Gb")
    print(f"Percentage: {svmem.percent}%")

def print_disk_info():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size: {partition_usage.total / (1024 * 1024 * 1024)}Gb")
        print(f"  Used: {partition_usage.used / (1024 * 1024 * 1024)}Gb")
        print(f"  Free: {partition_usage.free / (1024 * 1024 * 1024)}Gb")
        print(f"  Percentage: {partition_usage.percent}%")

def print_battery_info():
    battery = psutil.sensors_batteries()
    if not battery or platform.system() == "Windows":  # for non-laptop devices
        print("Battery not available.")
    else:
        for b in battery:
            print(f"Battery Percentage: {b.percent}%")
            print(f"Battery Status: {b.status}")
            print(f"Battery Sections: {b.sections}")

def print_power_supply_info():
    try:
        if platform.system() == "Linux":
            output = subprocess.check_output(["upower", "-i", "/org/freedesktop/UPower/devices/line_power_supply"], universal_newlines=True)
        elif platform.system() == "Windows":
            output = subprocess.check_output(["powercfg", "/qh"], universal_newlines=True)
        elif platform.system() == "Darwin":  # for macOS
            output = "Power supply info not available on macOS."
        else:
            print("Power supply info not available for this platform.")
            return
        print(output)
    except subprocess.CalledProcessError:
        print("Power supply info not available.")

def print_temperature():
    sensor_list = psutil.sensors_temperatures()
    for name, data in sensor_list.items():
        print(f"=== {name} ===")
        for item in data:
            print(f"  Current: {item.current} °C")
            print(f"  High: {item.high} °C")
            print(f"  Label: {item.label}")

if __name__ == "__main__":
    print_system_info()
    print_cpu_info()
    print_memory_info()
    print_disk_info()
    print_battery_info()
    print_power_supply_info()
    print_temperature() 