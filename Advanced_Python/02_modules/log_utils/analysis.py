from .parser import parse_log

def analyze_logs(logs):

    level_counts = {
        "INFO":0,
        "WARNING":0,
        "ERROR":0
    }

    error_users = set()
    unique_errors = set()

    error_frequency = {}
    user_error_frequency = {}

    invalid_logs = 0

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

            # error frequency
            error_frequency[message] = (error_frequency.get(message,0)+1)

            # user error frequency
            user_error_frequency[user] =(user_error_frequency.get(user,0)+1)

        # most frequent error
        if error_frequency:
            most_frequent_error = max(error_frequency,key=error_frequency.get)
        else:
            most_frequent_error = None

        # user with most errors
        if user_error_frequency:top_error_user = max(user_error_frequency, key = user_error_frequency.get)
        else:
            top_error_user = None

        # sort users by umber of errors
        sorted_error_users = sorted(user_error_frequency.items(), key=lambda item:item[1],reverse = True)

    return {
        "INFO":level_counts["INFO"],
        "WARNING":level_counts["WARNING"],
        "ERROR":level_counts["ERROR"],
        "error_users":error_users,
        "unique_errors":unique_errors,
        "error_frequency":error_frequency,
        "top_error_user":top_error_user,
        "most_frequent_error":most_frequent_error,
        "sorted_error_users":sorted_error_users,
        "invalid_logs": invalid_logs
    }

