from fastapi import APIRouter, HTTPException, Path, Body, status, Depends
from typing import List
from app.schemas.investment import InvestmentCreate, InvestmentUpdate, InvestmentOut
from app.services import investment as crud_investment
from app.dependencies.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/investments/", response_model=InvestmentOut, status_code=status.HTTP_201_CREATED)
def create_investment(investment: InvestmentCreate, db: Session = Depends(get_db)):
    # Logic to create an investment
    try:
        return crud_investment.create_user_investment(db, investment, investment.user_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/investments/", response_model=List[InvestmentOut])
def read_investments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Logic to read investments
    return crud_investment.get_investments(db, skip=skip, limit=limit)


@router.get("/investments/{investment_id}", response_model=InvestmentOut)
def read_investment(investment_id: int = Path(..., description="The ID of the investment to get"), db: Session = Depends(get_db)):
    # Logic to get a single investment by ID
    return crud_investment.get_investment(db, investment_id)


@router.put("/investments/{investment_id}", response_model=InvestmentOut)
def update_investment(investment_id: int, investment: InvestmentUpdate, db: Session = Depends(get_db)):
    # Logic to update an investment
    try:
        updated_investment = crud_investment.update_investment(db, investment_id, investment)
        if updated_investment is None:
            raise HTTPException(status_code=404, detail="Investment not found")
        return updated_investment
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/investments/{investment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_investment(investment_id: int, db: Session = Depends(get_db)):
    # Logic to delete an investment
    return crud_investment.delete_investment(db, investment_id)
