from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
from models.session import Session
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, session_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.session.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    booking.id = id