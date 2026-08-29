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
    print("\nError frequency:" , result["error_frequency"])
    print("\ntop error user:" , result["top_error_user"])
    print("\nmost frequent error:" , result["most_frequent_error"])
    print("\nsorted error users:" , result["sorted_error_users"])
    print("\ninvalid logs:" , result["invalid_logs"])


if __name__ == "__main__":
    main()


