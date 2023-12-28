from flask import Flask, request, jsonify
from flask_cors import CORS
from algorithms.friends_graph.graph_funcs import calc_social_index_students

app = Flask(__name__)
CORS(app)  # הפעלת CORS

@app.route('/calculate_social_index', methods=['POST'])
def calculate_social_index():
    print("enter server python")
    # קבלת מידע מהבקשה (אם יש)
    data = request.get_json()
    print("*******************************************************",data)
    # חישוב המדד החברתי באמצעות הפונקציה המיובאת
    result = calc_social_index_students(data['friends_list'])

    # החזרת התוצאה בתור JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)