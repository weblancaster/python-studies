"""
Day 31
I got some work for work so here is a quick flask API
"""
import os

from flask import Flask, jsonify, request
app = Flask(__name__)

STUDENTS = [
    {
        "id": 1,
        "name": "jon doe",
        "school": "engineering"
    },
    {
        "id": 2,
        "name": "jane doe",
        "school": "engineering"
    }
]

@app.route("/students")
def get_students():
    return jsonify({
        "data": STUDENTS
    })

@app.route("/students/<number:index>")
def get_student_by_id(index):
    student = [student for student in STUDENTS if index == student["id"]]

    return jsonify({
        "data": student[0]
    })


if __name__ == "__main__":
    PORT = os.getenv("PORT", 5000)
    app.run(port=PORT)
