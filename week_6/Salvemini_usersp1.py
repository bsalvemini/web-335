"""
Author: Brandon Salvemini
Date: 7/3/2024
File Name: Salvemini_usersp1.py
Description: Python program that connects to a MongoDB databases and performs some queries
"""

#import MongoClient
from pymongo import MongoClient

# Build a connection string to connect to client
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.lcwc1ht.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity")

# Variable to access the web333DB database
db = client['web335DB']

# Displays all users in the users collection by looping through them
for user in db.users.find():
    print (user)

# Extra print statement to put a new line before the next query to separate them
print()

# Display the document where the employeeId is 1011
print(db.users.find_one({"employeeId": "1011"}))

# Extra print statement to put a new line before the next query to separate them
print()

# Display the document where the lastName is Mozart
print(db.users.find_one({"lastName": "Mozart"}))