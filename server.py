from flask import Flask, request, jsonify
from flask_cors import CORS
from algorithms.friends_graph.graph_funcs import calc_social_index_students
from algorithms.friends_graph.calculate_social_index import calculate_social_index as calc_social_index_algorithm

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/calculate_social_index', methods=['POST'])
def calculate_social_index_route():
    data = request.get_json()

    # Extracting data arrays from respective records
    attendance_data = data['attendance_record']['data']

    grades_data = data['grades_record']['data']

    important_messages_data = data['important_messages_record']['data']['studentsWithImportantMessages']

    # Mapping attendance data to a dictionary
    dict_attendance = {student['student']: student['down'] for student in attendance_data}
    dict_grades = {student['student']: student['down'] for student in grades_data}
    dict_important_messages = {student['student']: student['hasImportantMessage'] for student in important_messages_data}

    # Assuming this function exists and works correctly
    survey_answers = calc_social_index_students(data['friends_list'])

    # Assuming this function exists and works correctly
    student_scores = calc_social_index_algorithm(dict_important_messages, dict_attendance, dict_grades, survey_answers)

    return jsonify(student_scores)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
