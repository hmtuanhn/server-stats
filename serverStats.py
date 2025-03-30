import psutil
import time
import datetime

def get_size(bytes, suffix="B"):
    """Convert bytes to a readable format (e.g. KB, MB, GB)."""
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def log_server_stats():
    print(f"\n===== Server Performance Stats at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} =====")

    # CPU
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"CPU Cores: {psutil.cpu_count(logical=True)} (Logical), {psutil.cpu_count(logical=False)} (Physical)")

    # Memory
    mem = psutil.virtual_memory()
    print(f"Memory Usage: {mem.percent}%")
    print(f"Total: {get_size(mem.total)}, Used: {get_size(mem.used)}, Free: {get_size(mem.available)}")

    # Swap Memory
    swap = psutil.swap_memory()
    print(f"Swap Usage: {swap.percent}%, Total: {get_size(swap.total)}, Used: {get_size(swap.used)}")

    # Disk
    print("\nDisk Usage:")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(f"  {part.device} - {part.mountpoint}: {usage.percent}% used ({get_size(usage.used)} / {get_size(usage.total)})")
        except PermissionError:
            continue

    # Network
    net = psutil.net_io_counters()
    print(f"\nNetwork I/O: Sent = {get_size(net.bytes_sent)}, Received = {get_size(net.bytes_recv)}")

if __name__ == "__main__":
    while True:
        log_server_stats()
        time.sleep(10)  # Refresh every 10 seconds aaa