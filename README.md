# <h2>PythonProject
Gym management app developed using Python, PostgreSQL, HTML/CSS and Flask

# <h3>Brief
A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

MVP
<ul>
<li>The app should allow the gym to create and edit Members
<li>The app should allow the gym to create and edit Classes
<li>The app should allow the gym to book members on specific classes
<li>The app should show a list of all upcoming classes
<li>The app should show all members that are booked in for a particular class
</ul>

Inspired By
Glofox, Pike13

Possible Extensions
<ul>
<li>Classes could have a maximum capacity, and users can only be added while there is space remaining.
<li>The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
<li>The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings.
</ul>

# <h3>Running Instructions
From the project's root folder in terminal:
<ul>
<li>createdb gym_manager
<li>psql -d gym_manager -f db/gym_manager.sql
</ul>

To input data into the database using the console:
<ul>
<li>python3 console.py
</ul>

To run the app:
<ul>
<li>flask run
</ul>

