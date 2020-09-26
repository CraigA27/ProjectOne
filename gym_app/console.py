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

session_1 = Session("HIIT Circuit", "2020/10/10", "18:30" , 30, 5)
session_repository.save(session_1)

pdb.set_trace()