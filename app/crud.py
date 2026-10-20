from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models import Bank, Branch


def get_banks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Bank).offset(skip).limit(limit).all()


def get_bank_by_id(db: Session, bank_id: int):
    return db.query(Bank).filter(Bank.id == bank_id).first()


def get_branches(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return db.query(Branch).offset(skip).limit(limit).all()


def get_branch_by_ifsc(db: Session, ifsc: str):
    return db.query(Branch).filter(Branch.ifsc == ifsc).first()


def search_branches(
    db: Session,
    query: str,
    skip: int = 0,
    limit: int = 100
):
    search_term = f"%{query}%"

    return (
        db.query(Branch)
        .filter(
            or_(
                Branch.branch.ilike(search_term),
                Branch.address.ilike(search_term),
                Branch.city.ilike(search_term),
                Branch.district.ilike(search_term),
                Branch.state.ilike(search_term),
                Branch.ifsc.ilike(search_term),
            )
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_branches_by_bank(
    db: Session,
    bank_id: int,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Branch)
        .filter(Branch.bank_id == bank_id)
        .offset(skip)
        .limit(limit)
        .all()
    )