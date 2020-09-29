from db.run_sql import run_sql
from models.session import Session
from models.member import Member

def save(session):
    sql = "INSERT INTO sessions ( name, date, time, duration, capacity ) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [session.name, session.date, session.time, session.duration, session.capacity]
    results = run_sql(sql, values)
    session.id = results[0]["id"]
    return session

def select_all():
    sessions = []
    
    sql = "SELECT * FROM sessions"
    results = run_sql(sql)
    for row in results:
        session = Session(row["name"], row["date"], row["time"], row["duration"], row["capacity"], row["id"])
        sessions.append(session)
    return sessions

def select_all_by_date():
    sessions = []
    
    sql = "SELECT * FROM sessions ORDER BY date, time ASC"
    results = run_sql(sql)
    for row in results:
        session = Session(row["name"], row["date"], row["time"], row["duration"], row["capacity"], row["id"])
        sessions.append(session)
    return sessions

def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        session = Session(result["name"], result["date"], result["time"], result["duration"], result["capacity"], result["id"])
    return session

def update(session):
    sql = "UPDATE sessions SET ( name, date, time, duration, capacity ) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [session.name, session.date, session.time, session.duration, session.capacity, session.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM sessions WHERE id =%s"
    values = [id]
    run_sql(sql, values)

def members(session):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE session_id = %s ORDER BY name"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row["name"], row["age"], row["membership"], row["status"], row["id"])
        members.append(member)
    return members 



