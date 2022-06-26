import logging
from contextlib import contextmanager
from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Numeric,
    Integer,
    String,
    Boolean,
)
from sqlalchemy.orm import registry, relationship, Session
from sqlalchemy.ext.hybrid import hybrid_property
from utils.string_formatters import nip_format, account_format, zip_code_format

engine = create_engine("sqlite+pysqlite:///data.db")
mapper_registry = registry()


@mapper_registry.mapped
class User:
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    company_name = Column(String)
    street = Column(String)
    city = Column(String)
    _zip_code = Column(String)
    _nip = Column(String)
    _account_number = Column(String)  # should be int
    bills = relationship("Bill", back_populates="user")

    @hybrid_property
    def nip(self):
        return nip_format(self._nip)

    @nip.setter
    def nip(self, value):
        self._nip = value

    @hybrid_property
    def zip_code(self):
        return zip_code_format(self._zip_code)

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value

    @hybrid_property
    def account_number(self):
        return account_format(self._account_number)

    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    def __repr__(self):
        return f"User: {self.first_name} {self.last_name}"

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'company_name': self.company_name,
            'street': self.street,
            'city': self.city,
            'zip_code': self.zip_code,
            'nip': self.nip,
            'account_number': self.account_number
        }

@mapper_registry.mapped
class Contractor:
    __tablename__ = "contractor"

    id = Column(Integer, primary_key=True)
    default = Column(Boolean, default=True, nullable=False)
    deleted = Column(Boolean, default=False, nullable=False)
    company_name = Column(String, nullable=False)
    _nip = Column(String, nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    _zip_code = Column(String, nullable=False)
    bills = relationship("Bill", back_populates="contractor")

    @hybrid_property
    def nip(self):
        return nip_format(self._nip)

    @nip.setter
    def nip(self, value):
        self._nip = value

    @hybrid_property
    def zip_code(self):
        return zip_code_format(self._zip_code)

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value

    def __str__(self):
        return f"{self.company_name}"

    def __repr__(self):
        return f"Contractor: {self.company_name}"

    def to_json(self):
        return {
            'default': self.default,
            'company_name': self.company_name,
            'nip': self._nip,
            'street': self.street,
            'city': self.city,
            'zip_code': self.zip_code,
        }

@mapper_registry.mapped
class ServiceAssociation:
    __tablename__ = 'association'
    service_id = Column(Integer, ForeignKey('service.id'), primary_key=True)
    bill_id = Column(Integer, ForeignKey('bill.id'), primary_key=True)
    service = relationship("Service")
    partial_amount = Column(Numeric(precision=2))
    full_amount = Column(Numeric(precision=2))
    volume = Column(Integer)
    measure = Column(String(4))


@mapper_registry.mapped
class Service:
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Numeric(precision=2))
    deleted = Column(Boolean, default=False, nullable=False)
    percentage = Column(String(3))

    def __str__(self):
        return f"{self.name}"


@mapper_registry.mapped
class Bill:
    __tablename__ = "bill"

    id = Column(Integer, primary_key=True)
    deleted = Column(Boolean, default=False, nullable=False)
    name = Column(String)
    amount = Column(Numeric(precision=2))
    payment_date = Column(Date)
    created = Column(DateTime, default=datetime.now())
    user = relationship("User", back_populates="bills")
    user_id = Column(ForeignKey("user.id"))
    contractor = relationship("Contractor", back_populates="bills")
    contractor_id = Column(ForeignKey("contractor.id"))
    services = relationship("ServiceAssociation")

    def __repr__(self):
        return f"{self.name} - {self.amount}"


@contextmanager
def session_manager(engine, mapper_registry):

    session = Session(engine)
    mapper_registry.metadata.create_all(engine)

    try:
        yield session
        session.commit()
    except Exception as exception:
        session.rollback()
        logging.error(exception, exc_info=True)
        raise
    finally:
        session.close()
