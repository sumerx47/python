# Check whether the directory exists.
# Walk through it recursively using os.walk().
# Count all files.
# Count .txt, .csv, .log, .py.
# Find the largest file.
# Return everything in a dictionary.


import os

def analyze_directory(path):

    if not os.path.exists(path):
        return "Directory does not exist"
    if not os.path.isdir(path):
        return "given path is not a directory"

    total_files = 0

    txt_count = 0
    log_count = 0
    csv_count = 0
    py_count = 0


    largest_file = None
    largest_size = 0

    for root, directories, files in os.walk(path):
        for file in files:
            total_files += 1
            file_path = os.path.join(root,file) 

            # count file types
            if file.endswith(".txt"):
                txt_count += 1
            elif file.endswith(".log"):
                log_count += 1
            elif file.endswith(".csv"):
                csv_count += 1
            elif file.endswith(".py"):
                py_count += 1

            # find largest file
            size = os.path.getsize(file_path)

            if size > largest_size:
                largest_size = size
                largest_file = file_path

    result = analyze_directory(r"")

    print("total_files: ", result["total_files"])
















