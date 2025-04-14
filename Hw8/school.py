from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def get_csv_path(name):
    return os.path.join(DATA_DIR, f"{name}.csv")

def read_csv(name):
    path = get_csv_path(name)
    if not os.path.exists(path):
        return []
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def write_csv(name, data, fieldnames):
    path = get_csv_path(name)
    write_header = not os.path.exists(path)
    with open(path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(data)

def overwrite_csv(name, data, fieldnames):
    path = get_csv_path(name)
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def find_by_id(data, id):
    for row in data:
        if row['ID'] == id:
            return row
    return None

def delete_by_id(data, id):
    return [row for row in data if row['ID'] != id]

@app.route('/student', methods=['GET', 'POST', 'DELETE'])
def student():
    fieldnames = ['ID', 'Name', 'Email', 'Phone', 'Year', 'Status']
    if request.method == 'POST':
        data = request.get_json()
        for field in fieldnames:
            if field not in data:
                return jsonify({'error': f'{field} is required'}), 500
        write_csv('student', data, fieldnames)
        return jsonify({'message': 'Student added successfully'}), 201

    elif request.method == 'DELETE':
        id = request.get_json().get('id')
        if not id:
            return jsonify({'error': 'id is required'}), 500
        students = read_csv('student')
        updated = delete_by_id(students, id)
        overwrite_csv('student', updated, fieldnames)
        return jsonify({'message': 'Student deleted successfully'})

    elif request.method == 'GET':
        id = request.args.get('id')
        if not id:
            return jsonify({'error': 'id is required'}), 500
        students = read_csv('student')
        student = find_by_id(students, id)
        return jsonify(student) if student else jsonify({'error': 'Student not found'}), 404

@app.route('/teacher', methods=['GET', 'POST', 'DELETE'])
def teacher():
    fieldnames = ['ID', 'Name', 'Email', 'Phone']
    if request.method == 'POST':
        data = request.get_json()
        for field in fieldnames:
            if field not in data:
                return jsonify({'error': f'{field} is required'}), 500
        write_csv('teacher', data, fieldnames)
        return jsonify({'message': 'Teacher added successfully'}), 201

    elif request.method == 'DELETE':
        id = request.get_json().get('id')
        if not id:
            return jsonify({'error': 'id is required'}), 500
        teachers = read_csv('teacher')
        updated = delete_by_id(teachers, id)
        overwrite_csv('teacher', updated, fieldnames)
        return jsonify({'message': 'Teacher deleted successfully'})

    elif request.method == 'GET':
        id = request.args.get('id')
        teachers = read_csv('teacher')
        teacher = find_by_id(teachers, id)
        if not teacher:
            return jsonify({'error': 'Teacher not found'}), 404
        if request.args.get('count') == 'true':
            classes = read_csv('class')
            class_count = sum(1 for c in classes if c['TeacherID'] == id)
            teacher['count'] = class_count
        return jsonify(teacher)

@app.route('/class', methods=['GET', 'POST', 'DELETE'])
def class_endpoint():
    fieldnames = ['ID', 'Name', 'Department', 'TeacherID']
    if request.method == 'POST':
        data = request.get_json()
        required_fields = ['ID', 'Name', 'TeacherID']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'{field} is required'}), 500
        if 'Department' not in data:
            data['Department'] = 'Misc'
        write_csv('class', data, fieldnames)
        return jsonify({'message': 'Class added successfully'}), 201

    elif request.method == 'DELETE':
        id = request.args.get('id')
        if not id:
            return jsonify({'error': 'id is required'}), 500
        classes = read_csv('class')
        updated = delete_by_id(classes, id)
        overwrite_csv('class', updated, fieldnames)
        return jsonify({'message': 'Class deleted successfully'})

    elif request.method == 'GET':
        if request.args.get('count') == 'true':
            classes = read_csv('class')
            return jsonify({'count': len(classes)})
        id = request.args.get('id')
        if not id:
            return jsonify({'error': 'id is required'}), 500
        classes = read_csv('class')
        class_data = find_by_id(classes, id)
        return jsonify(class_data) if class_data else jsonify({'error': 'Class not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)