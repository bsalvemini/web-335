"""
Author: Brandon Salvemini
Date: 7/9/2024
File Name: Salvemini_usersp2.py
Description: Python program that connects to a MongoDB database and performs CRUD operations
"""

# import MongoClient and datetime
from pymongo import MongoClient
import datetime

# Build a connection string to connect to client
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.lcwc1ht.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity")

# Variable to access the web335DB database
db = client['web335DB']

# Create a new dictionary holding data for the new user
stravinsky = {
    "firstName":"Igor",
    "lastName": "Stravinsky",
    "employeeId":"1014",
    "email":"istravinsky@me.com",
    "dateCreated": datetime.datetime.now(datetime.UTC) # This was used instead of .utcnow because .utcnow has been deprecated
}

# Insert the document into the users collection and print the inserted_id
stravinsky_user_id = db.users.insert_one(stravinsky).inserted_id
print(stravinsky_user_id)

# Prove the insert worked by finding the employeeId of the newly inserted document
print(db.users.find_one({"employeeId":"1014"}))

# Create an update query to update the email of the document created above
db.users.update_one(
    {"employeeId":"1014"},
    {
        "$set":{
            "email": "stravinsky@me.com"
        }
    }
)

# Prove the update worked by finding the employeeId of the newly updated document
print(db.users.find_one({"employeeId":"1014"}))

# Create a delete query to delete the document created above
result = db.users.delete_one({
    "employeeId":"1014"
})

# Output the result of the query to the screen
print(result)

# Prove the delete worked by finding the employeeId of the newly deleted document
print(db.users.find_one({"employeeId":"1014"}))
