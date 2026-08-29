# this modle is responsible for converting a log file into a dictionary

def parse_log(line):
    parts = line.strip().split("|")

    if len(parts) != 3:
        raise ValueError("Invalid log format")

    level = parts[0].strip()
    user = parts[1].strip()
    message = parts[2].strip()

    if level not in {"INFO", "WARNING", "ERROR"}:
        raise ValueError("Invalid Log Level")

    return {
        "level":level,
        "user":user,
        "message":message
    }










