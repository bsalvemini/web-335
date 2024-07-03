// 2a Displays all students
db.students.find();

// 2b Adds a new student, proves it was added

// Adds new student
db.students.insertOne({"firstName": "Thomas", "lastName": "Paley", "studentId": "s1019", "houseId": "h1007"});

// To prove student was added
db.students.findOne({"studentId": "s1019"});

// 2c Update property of student added in step 2b

// Updates firstName property of the student with the id s1019
db.students.updateOne({"studentId": "s1019"}, {$set: {"firstName": "Tom"}});

// To prove the first name was updated
db.students.findOne({"studentId": "s1019"});

// 2d Delete the student added in step b

// Deletes student
db.students.deleteOne({"studentId": "s1019"});

// To prove student was deleted
db.students.findOne({"studentId": "s1019"});

// 2e Displays all students by house
db.houses.aggregate([{$lookup:{from:"students",localField:"houseId",foreignField:"houseId",as:"students_in_house"}}]);

// 2f Displays all students in house Gryffindor
db.houses.aggregate([{$match:{houseId:"h1007"}},{$lookup:{from:"students",localField:"houseId",foreignField:"houseId",as:"students_in_house"}}])

// 2g Displays all students in the house with an Eagle mascot
db.houses.aggregate([{$match:{mascot:"Eagle"}},{$lookup:{from:"students",localField:"houseId",foreignField:"houseId",as:"students_in_house"}}])
