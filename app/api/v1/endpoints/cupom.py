from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import commons

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/", response_model=List[schemas.Cupom])
async def get_cupons(
    db: AsyncSession = Depends(commons.get_db),
    skip: int = 0,
    limit: int = 100
    # current_user: models.User = Depends(commons.get_current_active_user),
) -> Any:
    """
    Retrieve items.
    """
    # if crud.user.is_superuser(current_user):
    #     cupons = crud.cupom.get_multi(db, skip=skip, limit=limit)
    # else:
    #     cupons = crud.cupom.get_multi_by_owner(
    #         db=db, owner_id=current_user.id, skip=skip, limit=limit
    #     )
    cupons = crud.cupom.get_multi(db, skip=skip, limit=limit)
    return await cupons


@router.post("/", response_model=schemas.Cupom)
async def create_cupom(
    *,
    db: AsyncSession = Depends(commons.get_db),
    cupom_in: schemas.CupomCreate
    # current_user: models.User = Depends(commons.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    cupom = crud.cupom.create(db=db, obj_in=cupom_in)
    return await cupom
    # cupom = crud.cupom.create_with_owner(db=db, obj_in=cupom_in, owner_id=current_user.id)
    # return await cupom


# @router.put("/{id}", response_model=schemas.Item)
# def update_item(
#     *,
#     db: Session = Depends(commons.get_db),
#     id: int,
#     item_in: schemas.ItemUpdate,
#     current_user: models.User = Depends(commons.get_current_active_user),
# ) -> Any:
#     """
#     Update an item.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
#     return item
#

@router.get("/{id}", response_model=schemas.Cupom)
async def get_item(
    *,
    db: AsyncSession = Depends(commons.get_db),
    id: int
    # current_user: models.User = Depends(commons.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    cupom = crud.cupom.get(db=db, id=id)
    if not cupom:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    return await cupom


# @router.delete("/{id}", response_model=schemas.Item)
# def delete_item(
#     *,
#     db: Session = Depends(commons.get_db),
#     id: int,
#     current_user: models.User = Depends(commons.get_current_active_user),
# ) -> Any:
#     """
#     Delete an item.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = crud.item.remove(db=db, id=id)
#     return item
