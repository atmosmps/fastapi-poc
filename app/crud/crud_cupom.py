from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.cupom import Cupom
from app.schemas.cupom import CupomCreate, CupomUpdate


class CRUDCupom(CRUDBase[Cupom, CupomCreate, CupomUpdate]):
    async def create_with_owner(
        self, db: Session, *, obj_in: CupomCreate, owner_id: int
    ) -> Cupom:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Cupom]:
        return (
            db.query(self.model)
            .filter(Cupom.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


cupom = CRUDCupom(Cupom)
