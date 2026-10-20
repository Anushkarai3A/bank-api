from pydantic import BaseModel, ConfigDict
from typing import Optional


class BankBase(BaseModel):
    name: str


class BankResponse(BankBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BranchBase(BaseModel):
    ifsc: str
    bank_id: int
    branch: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None


class BranchResponse(BranchBase):
    model_config = ConfigDict(from_attributes=True)