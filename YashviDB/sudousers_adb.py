from sqlalchemy import Column
from YashviDB import BASE, SESSION
from sqlalchemy.sql.sqltypes import BigInteger
import threading

class SUDO(BASE):
    __tablename__ = "sudousers"

    id = Column(BigInteger, primary_key=True)

    def __init__(self, id):
        self.id = id

SUDO.__table__.create(checkfirst=True)

SUDO_IL = threading.RLock()

def add_sudo(id):
    with SUDO_IL:
        is_sudo = SESSION.query(SUDO).get(id)
        if not is_sudo:
            adder = SUDO(id)
            SESSION.add(adder)
            SESSION.commit()
        else:
            SESSION.close()
    
def del_sudo(id):
    with SUDO_IL:
        is_sudo = SESSION.query(SUDO).get(id)
        if is_sudo:
            SESSION.delete(is_sudo)
            SESSION.commit()
        else:
            SESSION.close()

def list_sudo():
    sudos = SESSION.query(SUDO).all()
    try:
        return sudos
    finally:
        SESSION.close()

def is_sudo(id):
    sudo = SESSION.query(SUDO).get(id)
    if sudo:
        return True
    else:
        return False
