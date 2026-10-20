from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Bank(Base):
    __tablename__ = "banks"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(49), nullable=False)

    branches = relationship("Branch", back_populates="bank")


class Branch(Base):
    __tablename__ = "branches"

    ifsc = Column(String(11), primary_key=True, index=True)

    bank_id = Column(
        BigInteger,
        ForeignKey("banks.id"),
        nullable=False
    )

    branch = Column(String(74))
    address = Column(String(195))
    city = Column(String(50))
    district = Column(String(50))
    state = Column(String(26))

    bank = relationship("Bank", back_populates="branches")