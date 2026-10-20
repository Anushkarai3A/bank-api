from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

app = FastAPI(
    title="Bank API",
    description="API for searching Indian banks and their branches.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Bank API is running!"}


@app.get("/health/db")
def check_database(db: Session = Depends(get_db)):
    from sqlalchemy import text

    result = db.execute(text("SELECT 1")).scalar()

    return {
        "database": "connected" if result == 1 else "error"
    }


@app.get("/banks", response_model=list[schemas.BankResponse])
def list_banks(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    return crud.get_banks(db, skip=skip, limit=limit)


@app.get("/banks/{bank_id}", response_model=schemas.BankResponse)
def get_bank(
    bank_id: int,
    db: Session = Depends(get_db)
):
    bank = crud.get_bank_by_id(db, bank_id)

    if bank is None:
        raise HTTPException(status_code=404, detail="Bank not found")

    return bank


@app.get("/branches", response_model=list[schemas.BranchResponse])
def list_branches(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    return crud.get_branches(db, skip=skip, limit=limit)


@app.get("/branches/search", response_model=list[schemas.BranchResponse])
def search_branches(
    q: str = Query(..., min_length=1),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    return crud.search_branches(
        db, query=q, skip=skip, limit=limit
    )


@app.get("/branches/{ifsc}", response_model=schemas.BranchResponse)
def get_branch(
    ifsc: str,
    db: Session = Depends(get_db)
):
    branch = crud.get_branch_by_ifsc(db, ifsc.upper())

    if branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")

    return branch


@app.get(
    "/banks/{bank_id}/branches",
    response_model=list[schemas.BranchResponse]
)
def list_bank_branches(
    bank_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    bank = crud.get_bank_by_id(db, bank_id)

    if bank is None:
        raise HTTPException(status_code=404, detail="Bank not found")

    return crud.get_branches_by_bank(
        db, bank_id=bank_id, skip=skip, limit=limit
    )