def get_max_average(grades_list):
    student_grades = {}

    for student, grade in grades_list:
        grade = int(grade)
        if student not in student_grades:
            student_grades[student] = [grade]
        else:
            student_grades[student].append(grade)

    max_avg = 0
    for student in student_grades:
        total = sum(student_grades[student])
        count = len(student_grades[student])
        avg = total / count
        if avg > max_avg:
            max_avg = avg

    return int(max_avg)

# Sample input
data = [
    ["Rachel", "100"],
    ["Phoebe", "80"],
    ["Monica", "95"],
    ["Rachel", "50"],
    ["Phoebe", "60"]
]

print(get_max_average(data))  # Expected output: 95
