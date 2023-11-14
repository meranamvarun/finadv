from pydantic import BaseModel


class RelationshipBase(BaseModel):
    user_id: int
    relative_id: int
    relationship_type: str
    can_view_portfolio: bool


class RelationshipCreate(RelationshipBase):
    pass


class Relationship(RelationshipBase):
    id: int

    class Config:
        orm_mode = True
