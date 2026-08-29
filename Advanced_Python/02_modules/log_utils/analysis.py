from .parser import parse_log

def analyze_logs(logs):

    level_counts = {
        "INFO":0,
        "WARNING":0,
        "ERROR":0
    }

    error_users = set()
    unique_errors = set()


    for line in logs:
        try:
            log = parse_log(line)
        except ValueError:
            invalid_logs += 1
            continue

        level = log["level"]
        user = log["user"]
        message = log["message"]

        # count log levels
        level_counts[level] += 1

        # process Error logs
        if level == "ERROR":

            # unique users
            error_users.add(user)

            # unique error messages
            unique_errors.add(message)






    return {
        "INFO":level_counts["INFO"],
        "WARNING":level_counts["WARNING"],
        "ERROR":level_counts["ERROR"],
        "error_users":error_users,
        "unique_errors":unique_errors,
    }

