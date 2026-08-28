from .calculations import calculate_average,get_grade

def analyze_students(students):
    # 1. calculate avg of every student
    averages = {student["name"]:round(calculate_average(student["marks"]),1) for student in students}

    # 2 calculate grade for every student
    grades = {student["name"]:get_grade(calculate_average(student["marks"])) for student in students}


    return {
        "averages":averages,
        "grades":grades
    }







