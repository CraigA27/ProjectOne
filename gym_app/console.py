import pdb
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import repositories.booking_repository as booking_repository

member_1 = Member("Arnold", 25, "Gold", True)
member_repository.save(member_1)

member_2 = Member("Bob", 32, "Silver", False)
member_repository.save(member_2)

session_1 = Session("HIIT Circuit", "2020-10-01", "18:30", 30, 5)
session_repository.save(session_1)

session_2 = Session("Yoga", "2020-10-01", "10:00", 60, 20)
session_repository.save(session_2)

booking_1 = Booking(member_1, session_1)
booking_repository.save(booking_1)

booking_2 = Booking(member_2, session_1)
booking_repository.save(booking_2)

pdb.set_trace()