import flightmanagement.dao
from datetime import datetime
from flightmanagement import db
from flightmanagement.models import *
import hashlib


def load_province():
    return Province.query.all()


def load_flight_booking(start_location, end_location, departure):
    flights = Flight.query.filter(Flight.active.__eq__(True))
    if flightmanagement.utils.load_active_flight_booking().__eq__(True):
        start_locations = Route.start_location.__eq__(start_location)
        end_location = Route.end_location.__eq__(end_location)

        if start_locations and end_location:
            flights = flights.filter(Flight.route.any(start_locations))
            flights = flights.filter(Flight.route.any(end_location))
            print(flights)
        if departure:
            d = datetime.strptime(departure, "%m/%d/%Y")
            print(d.year)
            start_time = Flight.start_time
            start_time = start_time.date
            flights = flights.filter.any(start_time.__eq__(departure))

    return flights.all()


def load_airport():
    return Airport.query.all()


def load_type_of_position():
    pos_type = TypeOfPosition.query.filter(TypeOfPosition.active.__eq__(True))
    return pos_type.all()


def load_route():
    return Route.query.all()


def load_pricing():
    return Pricing.query.all()


def load_discount():
    return Discount.query.all()


def register(name, username, password, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(username=username.strip(),
             password=password, avatar=avatar)
    db.session.add(u)
    db.session.commit()


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)
