from log_utils.analysis import analyze_logs

logs = [
    "INFO|Ayaan|Login successful",
    "ERROR|Sara|Database connection failed",
    "WARNING|Zaid|Disk usage high",
    "INFO|Maryam|Login successful",
    "ERROR|Ayaan|Authentication failed",
    "ERROR|Sara|Database connection failed",
    "INFO|Zaid|Logout successful",
    "WARNING|Maryam|Memory usage high",
    "ERROR|Ayaan|Authentication failed"
]

def main():
    result = analyze_logs(logs)
    print("INFO:", result["INFO"])
    print("WARNING:", result["WARNING"])
    print("ERROR:", result["ERROR"])
    print("\nError Users:" , result["error_users"])
    print("\nUnique Errors:" , result["unique_errors"])






if __name__ == "__main__":
    main()


