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
    zip_code = Column(String)
    nip = Column(String)  # should be int
    account_number = Column(String)  # should be int
    contractors = relationship("Contractor", back_populates="user")
    bills = relationship("Bill", back_populates="user")

    def __repr__(self):
        return f"User: {self.first_name} {self.last_name}"


@mapper_registry.mapped
class Contractor:
    __tablename__ = "contractor"

    id = Column(Integer, primary_key=True)
    default = Column(Boolean, default=True, nullable=False)
    deleted = Column(Boolean, default=False, nullable=False)
    company_name = Column(String, nullable=False)
    nip = Column(Integer, nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    user = relationship("User", back_populates="contractors")
    user_id = Column(ForeignKey("user.id"))
    bills = relationship("Bill", back_populates="contractor")

    def __str__(self):
        return f"{self.company_name}"

    def __repr__(self):
        return f"Contractor: {self.company_name}"


@mapper_registry.mapped
class ServiceAssociation:
    __tablename__ = 'association'
    service_id = Column(Integer, ForeignKey('service.id'), primary_key=True)
    bill_id = Column(Integer, ForeignKey('bill.id'), primary_key=True)
    extra_data = Column(String(50))
    service = relationship("Service")


@mapper_registry.mapped
class Service:
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Numeric(precision=2))


@mapper_registry.mapped
class Bill:
    __tablename__ = "bill"

    id = Column(Integer, primary_key=True)
    deleted = Column(Boolean, default=False, nullable=False)
    name = Column(String)
    amount = Column(Numeric(precision=2))
    signature = Column(String)
    payment_date = Column(Date)
    created = Column(DateTime, default=datetime.now())
    user = relationship("User", back_populates="bills")
    user_id = Column(ForeignKey("user.id"))
    contractor = relationship("Contractor", back_populates="bills")
    contractor_id = Column(ForeignKey("contractor.id"))
    services = relationship("ServiceAssociation")

    def __repr__(self):
        return f"{self.signature} - {self.amount}"


@contextmanager
def session_manager(engine, mapper_registry):

    session = Session(engine)
    mapper_registry.metadata.create_all(engine)

    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

