from .calculations import calculate_average,get_grade

def analyze_students(students):
    # 1. calculate avg of every student
    averages = {student["name"]:round(calculate_average(student["marks"]),1) for student in students}

    # 2 calculate grade for every student
    grades = {student["name"]:get_grade(calculate_average(student["marks"])) for student in students}

    # 3 find eligible students 
    eligible_students = [student["name"] for student in students if (student["active"] and student["attendance"] >= 80 and calculate_average(student["marks"]) >= 75) ]

    # 4 find highest average student
    highest = max(students, key = lambda student:calculate_average(student["marks"]))
    highest_student = (highest["name"],round(calculate_average(highest["marks"]),1))

    # 5 find lowest average student 
    lowest = min(students, key = lambda student:calculate_average(student["marks"]))
    lowest_student = (lowest["name"], round(calculate_average(lowest["marks"]),1))

    # 6 find all unique skills
    all_skills = [skill for student in students for skill in student["skills"]]

    # 7 find qualifying students
    qualifying_students = [student for student in students if (student["active"] and student["attendance"] >= 80 and calculate_average(student["marks"]) >= 75)] 

    # 8 find skills common to all qualifying students



    return {
        "averages":averages,
        "grades":grades,
        "eligible_students":eligible_students,
        "highest_student":highest_student,
        "lowest_student":lowest_student,
        "all_skills":all_skills,
        "qualifying_students":qualifying_students



    }







