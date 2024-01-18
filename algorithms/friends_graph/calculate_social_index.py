def calculate_social_index(dict_attendance, dict_grades, dict_important_messages, survey_answers):
    social_index = {}

    for student_id in set(dict_attendance.keys()) | set(dict_grades.keys()) | set(dict_important_messages.keys()):
        attendance_value = 0.2 if dict_attendance.get(student_id, True) else 0
        grades_value = 0.2 if dict_grades.get(student_id, False) else 0
        messages_value = 0.1 if dict_important_messages.get(student_id, False) else 0
        survey_value = survey_answers.get(student_id, 0) * 0.5

        score = attendance_value + grades_value + messages_value + survey_value
        social_index[student_id] = score

    return social_index

# # הקריאה לפונקציה עם המילונים הנתונים שלך
# new_social_index = calculate_social_index(dict_attendance, dict_grades, dict_important_messages, survey_answers)
# print(new_social_index)
