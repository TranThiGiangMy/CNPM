import hashlib
from flightmanagement import app, dao
from datetime import timedelta, datetime
from flightmanagement.models import *


def load_active_flight_booking():
    local_time = datetime.now()
    exp_time = local_time + timedelta(hours=12)
    if Flight.query.filter(Flight.start_time.__le__(exp_time)):
        return False
    return True


def load_active_flight_sale():
    local_time = datetime.now()
    exp_time = local_time + timedelta(hours=4)
    if Flight.query.filter(Flight.start_time.__le__(exp_time)):
        return Flight.active.__eq__(False)
    return Flight.active.__eq__(True)
