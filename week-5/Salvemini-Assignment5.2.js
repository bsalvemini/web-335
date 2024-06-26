// 1a Adds a new user to the collection, prove it was added

// Adds new user
db.users.insertOne({"firstName":"Antonio", "lastName": "Vivaldi", "employeeId":"1013", "email":"avivaldi@me.com", "dateCreated": new Date()});

// To prove the new user was added
db.users.findOne({"lastName": "Vivaldi"});

// 2a Updates Mozart's email address to mozart@me.com, prove it was updated

// Updates Mozart's email address to mozart@me.com
db.users.updateOne({"lastName": "Mozart" }, {"$set":{"email": "mozart@me.com"}});

// To prove the email was updated
db.users.findOne({"lastName": "Mozart"});

// 3a Display all users in the collection, shows only the first name, last name, and email address
// This is based on the information in the "Specifying Which Keys To Return" section of Chapter 4 of The Definitive Guide

db.users.find({}, {"firstName": 1, "lastName": 1, "email": 1, "_id": 0});