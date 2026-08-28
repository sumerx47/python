from student_utils.analysis import analyze_students


students = [
    {
        "name": "Ayaan",
        "marks": [78, 85, 92, 67, 88],
        "attendance": 91.5,
        "active": True,
        "skills": {"Python", "SQL", "Excel"}
    },
    {
        "name": "Sara",
        "marks": [95, 89, 93, 90, 96],
        "attendance": 96.0,
        "active": True,
        "skills": {"Python", "PowerBI", "SQL"}
    },
    {
        "name": "Zaid",
        "marks": [55, 62, 48, 70, 59],
        "attendance": 72.5,
        "active": False,
        "skills": {"Excel", "C"}
    },
    {
        "name": "Maryam",
        "marks": [88, 76, 91, 84, 79],
        "attendance": 88.0,
        "active": True,
        "skills": {"Python", "Java", "SQL"}
    }
]


def main():
    result = analyze_students(students)
    print("Averages: ", result["averages"])
    print("\nGrades: ", result["grades"])
    print("\nEligible students: ", result["eligible_students"])
    print("\nHighest student: ", result["highest_student"]) 
    print("\nLowest student: ", result["lowest_student"]) 
    print("\nAll Skills: ", set(result["all_skills"])) 
    print("\nQualifying students: ", result["qualifying_students"]) 
    print("\nCommon skills: ", result["common_skills"]) 
    print("\nSorted students: ", result["sorted_students"]) 
    print("\nStudent results: ", result["student_results"]) 





'''    for student in result["student_results"]:
        print(student)'''


if __name__ == "__main__":
    main()


