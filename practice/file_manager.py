import json
from student import Student

FILE_NAME = "students.json"

def save_students(students):
    data = [student.to_dict() for student in students]
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Student.from_dict(item) for item in data]
    except FileNotFoundError:
        return []