#Day 29: 30 Days of python programming

from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

MONGODB_URI = 'mongodb+srv://porsiaca62:testmongo@cluster0.nfd8zpq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']

# Get all students
@app.route('/api/v1.0/students', methods=['GET'])
def students():
    students = db.students.find()  # Fetch all students
    return Response(dumps(students), mimetype='application/json')

# Get a single student by ID
@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    student = db.students.find_one({'_id': ObjectId(id)})  # Fetch one student by ID
    return Response(dumps(student), mimetype='application/json')

# Create a new student
@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()

    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }

    db.students.insert_one(student)
    return Response(dumps({"result": "Student created successfully"}), mimetype='application/json')

# Update an existing student's information
@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    query = {"_id": ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()

    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }

    db.students.update_one(query, {"$set": student})
    return Response(dumps({"result": "Student updated successfully"}), mimetype='application/json')

# Delete a student by ID
@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    db.students.delete_one({"_id": ObjectId(id)})
    return Response(dumps({"result": "Student deleted successfully"}), mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5002))
    app.run(debug=True, host='0.0.0.0', port=port)