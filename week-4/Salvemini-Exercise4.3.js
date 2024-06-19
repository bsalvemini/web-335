// 7a Display all users in the collection

db.users.find();

// 7b Display the user with the email address jbach@me.com

db.users.findOne({ email: 'jbach@me.com' });

// 7c Display the user with the last name Mozart

db.users.findOne({ lastName: 'Mozart' });

// 7d Display the user with the first name Richard

db.users.findOne({ firstName: 'Richard' });

// 7e Display the user with employeeId 1010

db.users.findOne({ employeeId: '1010' });
