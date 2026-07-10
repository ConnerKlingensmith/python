import time
import re
from collections import Counter
from functools import wraps


# Decorator to measure execution time
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        print(f"{func.__name__} executed in "
              f"{end_time - start_time:.6f} seconds")

        return result

    return wrapper


# Generator function
def parse_log_file(filename):
    """
    Yields log entries one at a time as dictionaries.
    Format:
    YYYY-MM-DD HH:MM:SS LEVEL Message
    """
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(maxsplit=3)

            if len(parts) < 4:
                continue

            yield {
                "timestamp": f"{parts[0]} {parts[1]}",
                "level": parts[2],
                "message": parts[3]
            }


@timer
def analyze_logs(filename):
    # Convert generator output to a list for multiple analyses
    logs = list(parse_log_file(filename))

    # List comprehension: Extract ERROR messages
    error_messages = [
        log["message"]
        for log in logs
        if log["level"] == "ERROR"
    ]

    # Dictionary comprehension: Count messages per level
    level_counts = {
        level: sum(
            1 for log in logs
            if log["level"] == level
        )
        for level in {log["level"] for log in logs}
    }

    # Set comprehension: Extract unique IP addresses
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

    unique_ips = {
        ip
        for log in logs
        for ip in re.findall(ip_pattern, log["message"])
    }

    print("\nERROR Messages:")
    for msg in error_messages:
        print(f"- {msg}")

    print("\nMessage Count by Level:")
    for level, count in level_counts.items():
        print(f"{level}: {count}")

    print("\nUnique IP Addresses:")
    for ip in unique_ips:
        print(ip)


# Example usage
if __name__ == "__main__":

    sample_logs = """2024-01-01 10:00:00 INFO Server started on 192.168.1.10
2024-01-01 10:01:23 ERROR Connection failed from 10.0.0.5
2024-01-01 10:02:45 WARN High memory usage
2024-01-01 10:03:12 ERROR Timeout from 10.0.0.5
"""

    with open("network.log", "w") as file:
        file.write(sample_logs)

    analyze_logs("network.log")
