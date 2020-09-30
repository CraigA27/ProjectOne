import pdb
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import repositories.booking_repository as booking_repository

member_1 = Member("Ada Armstrong", 25, "Premium", True)
member_repository.save(member_1)

member_2 = Member("Gary Goodbody", 32, "Standard", False)
member_repository.save(member_2)

member_3 = Member("Larry Liftsalot", 40, "Standard", True)
member_repository.save(member_3)

session_1 = Session("HIIT Circuit", "2020-10-04", "18:30", 30, 5)
session_repository.save(session_1)

session_2 = Session("Yoga", "2020-10-02", "10:00", 60, 15)
session_repository.save(session_2)

session_3 = Session ("Boxing", "2020-10-02", "17:30", 30, 5)
session_repository.save(session_3)

booking_1 = Booking(member_1, session_1)
booking_repository.save(booking_1)

booking_2 = Booking(member_2, session_1)
booking_repository.save(booking_2)

booking_3 = Booking(member_1, session_2)
booking_repository.save(booking_3)

pdb.set_trace()