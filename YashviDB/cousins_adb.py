from sqlalchemy import Column
from YashviDB import BASE, SESSION
from sqlalchemy.sql.sqltypes import BigInteger
import threading

class Cousins(BASE):
    __tablename__ = "cousins"
    
    i_id = Column(BigInteger, primary_key=True)
    f_id = Column(BigInteger, primary_key=True)

    def __init__(self, i_id, f_id):
        self.i_id = i_id 
        self.f_id = f_id

class Wait(BASE):
    __tablename__ = "waiting"

    i_id = Column(BigInteger, primary_key=True)
    f_id = Column(BigInteger, primary_key=True)

    def __init__(self, i_id, f_id):
        self.i_id = i_id
        self.f_id = f_id

Cousins.__table__.create(checkfirst=True)

Wait.__table__.create(checkfirst=True)

COUSIN_LOCK = threading.RLock()

WAITING_LOCK = threading.RLock()

def add_cousin(i_id, f_id):
    with COUSIN_LOCK:
        if_c = SESSION.query(Cousins).get(i_id, f_id)
        if not if_c:
            one_c = Cousins(i_id, f_id)
            SESSION.add(one_c)
            SESSION.commit()

def are_cousins(i_id, f_id):
    try:
        SESSION.query(Cousins).get(i_id, f_id)
        return True
    except:
        SESSION.close()
        return False
        

def rmv_cousin(i_id, f_id):
    with COUSIN_LOCK:
        r_c = SESSION.query(Cousins).get(i_id, f_id)
        if r_c:
            SESSION.delete(r_c)
            SESSION.commit()

def cousins_list_for(i_id):
    try:
        return (
            SESSION.query(Cousins)
            .filter(Cousins.i_id == i_id)
            .order_by(Cousins.f_id.asc())
            .all()
        )
    finally:
        SESSION.close()

def add_to_waiting(i_id, f_id):
    with WAITING_LOCK:
        in_waiting = SESSION.query(Wait).get(i_id, f_id)
        if not in_waiting:
            adder = Wait(i_id, f_id)
            SESSION.add(adder)
            SESSION.commit()

def rmv_from_waiting(i_id, f_id):
    with WAITING_LOCK:
        in_waiting = SESSION.query(Wait).get(i_id, f_id)
        if in_waiting:
            SESSION.delete(in_waiting)
            SESSION.commit()  

def check_waiting_list(i_id, f_id):
    getter = SESSION.query(Wait).get(i_id, f_id)
    if getter:
        return True
    else:
        return False
