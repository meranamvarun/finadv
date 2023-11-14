from sqlalchemy.orm import Session
from app.models.user import User
from app.models.investment import Investment
from app.schemas.investment import InvestmentCreate, InvestmentUpdate


def get_investment(db: Session, investment_id: int):
    return db.query(Investment).filter(Investment.id == investment_id).first()


def get_investments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Investment).offset(skip).limit(limit).all()


def create_user_investment(db: Session, investment: InvestmentCreate, user_id: int):
    db_investment = Investment(**investment.dict())
    db.add(db_investment)
    db.commit()
    db.refresh(db_investment)
    return db_investment


def update_investment(db: Session, investment_id: int, investment: InvestmentUpdate):
    db_investment = get_investment(db, investment_id)
    if db_investment:
        update_data = investment.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_investment, key, value)
        db.add(db_investment)
        db.commit()
        db.refresh(db_investment)
        return db_investment
    return None


def delete_investment(db: Session, investment_id: int):
    db_investment = get_investment(db, investment_id)
    if db_investment:
        db.delete(db_investment)
        db.commit()
        return db_investment
    return None
