#Day 27: 30 Days of python programming

from flask import Flask
from bson import ObjectId  # Import ObjectId to use it in queries
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Get the MongoDB URI from environment variables
uri = os.environ.get('MONGODB_URI')

if not uri:
    raise ValueError("MONGODB_URI environment variable is not set!")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

if not uri:
    raise ValueError("MONGODB_URI environment variable is not set!")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Database selection
db = client['thirty_days_of_python']

# Insert a single document
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})

# Insert multiple documents
students = [
    {'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34},
    {'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28},
    {'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
]
db.students.insert_many(students)

# Find a student by _id
student = db.students.find_one({'_id': ObjectId('<some_id>')})  # Replace <some_id> with an actual ObjectId
print(student)

# Find students from Finland and print their name and country
students = db.students.find({'country': 'Finland'}, {'_id': 0, 'name': 1, 'country': 1})
for student in students:
    print(student)

# Update a student's age
query = {'age': 250}
new_value = {'$set': {'age': 38}}
db.students.update_one(query, new_value)

# Delete a student by name
query = {'name': 'John'}
db.students.delete_one(query)

# Sort students by age in descending order and limit to 3 results
students = db.students.find().sort('age', -1).limit(3)
for student in students:
    print(student)

# Initialize Flask app
app = Flask(__name__)

# Run Flask app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
