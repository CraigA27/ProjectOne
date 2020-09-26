DROP TABLE bookings;
DROP TABLE members;
DROP TABLE sessions;

CREATE TABLE members(
id SERIAL PRIMARY KEY,
name VARCHAR(255),
age INT,
membership VARCHAR(255),
status BOOLEAN
);

CREATE TABLE sessions(
id SERIAL PRIMARY KEY,
name VARCHAR(255),
date VARCHAR(255),
time VARCHAR(255),
duration INT,
capacity INT
);

CREATE TABLE bookings(
id SERIAL PRIMARY KEY,
member_id INT REFERENCES members(id) ON DELETE CASCADE,
session_id INT REFERENCES sessions(id) ON DELETE CASCADE
);