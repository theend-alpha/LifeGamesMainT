from sqlalchemy import Column
from YashviDB import BASE, SESSION
from sqlalchemy.sql.sqltypes import BigInteger
import threading

class SUDO(BASE):
    __tablename__ = sudousers

    id = Column(BigInteger, primary_key=True)

    def __init__(self, id):
        self.id = id

SUDO.__table__.create(checkfirst=True)

SUDO_IL = threading.RLock()

