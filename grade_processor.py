
# SUBMISSION CHECKLIST
# [x] 'grade' key added to every student dictionary
# [x] 'at_risk' boolean key added to every student dictionary
# [x] class_summary dictionary contains all 6 required keys
# [x] grade_distribution dictionary produced
# [x] at-risk report printed with reason for flag
# [x] top performer(s) identified and printed
# [x] no hardcoded outputs - all results computed by code
# [x] all variable names use snake_case


# 1. STARTING DATA (DO NOT MODIFY)
students = [
    {'name': 'Kofi Mensah', 'score': 87, 'attendance': 92},
    {'name': 'Ama Owusu', 'score': 54, 'attendance': 78},
    {'name': 'Kwame Asante', 'score': 73, 'attendance': 55},
    {'name': 'Abena Darko', 'score': 95, 'attendance': 98},
    {'name': 'Yaw Boateng', 'score': 61, 'attendance': 88},
    {'name': 'Efua Antwi', 'score': 48, 'attendance': 70},
    {'name': 'Nana Acheampong', 'score': 79, 'attendance': 91},
    {'name': 'Akua Frimpong', 'score': 66, 'attendance': 60}
]


# 2. GRADE CLASSIFICATION AND AT-RISK FLAG
for student in students:

    score = student['score']
    attendance = student['attendance']

    if score >= 90:
        student['grade'] = 'A'
    elif score >= 75:
        student['grade'] = 'B'
    elif score >= 60:
        student['grade'] = 'C'
    else:
        student['grade'] = 'F'

    student['at_risk'] = score < 60 or attendance < 65


# 3. CLASS SUMMARY DICTIONARY
total_students = len(students)

total_score = sum(student['score'] for student in students)

passing_count = sum(1 for student in students if student['score'] >= 60)

failing_count = total_students - passing_count

class_average = total_score / total_students

highest_score = max(student['score'] for student in students)

lowest_score = min(student['score'] for student in students)

class_summary = {
    'total_students': total_students,
    'passing_count': passing_count,
    'failing_count': failing_count,
    'class_average': round(class_average, 2),
    'highest_score': highest_score,
    'lowest_score': lowest_score
}


# 4. GRADE DISTRIBUTION
grade_distribution = {
    'A': 0,
    'B': 0,
    'C': 0,
    'F': 0
}

for student in students:
    grade_distribution[student['grade']] += 1


# 5. AT-RISK STUDENT REPORT
print("\n========== AT-RISK STUDENT REPORT ==========")

for student in students:

    if student['at_risk']:

        reasons = []

        if student['score'] < 60:
            reasons.append("Score below 60")

        if student['attendance'] < 65:
            reasons.append("Attendance below 65%")

        reason = " and ".join(reasons)

        print(f"Name: {student['name']}")
        print(f"Score: {student['score']}")
        print(f"Attendance: {student['attendance']}%")
        print(f"Reason: {reason}")
        print("--------------------------------------------")


# 6. TOP PERFORMER RECOGNITION
print("\n========== TOP PERFORMER(S) ==========")

for student in students:
    if student['score'] == highest_score:
        print(f"Name: {student['name']}")
        print(f"Score: {student['score']}")
        print(f"Grade: {student['grade']}")


# 7. DISPLAY CLASS SUMMARY
print("\n========== CLASS SUMMARY ==========")

for key, value in class_summary.items():
    print(f"{key}: {value}")


# 8. DISPLAY GRADE DISTRIBUTION
print("\n========== GRADE DISTRIBUTION ==========")

for grade, count in grade_distribution.items():
    print(f"Grade {grade}: {count} student(s)")


# 9. DISPLAY COMPLETE STUDENT RECORDS
print("\n========== COMPLETE STUDENT RECORDS ==========")

for student in students:
    print(student)
