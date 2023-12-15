from typing import Any, Generic, List, Optional, TypeVar

from sqlmodel import SQLModel
from sqlmodel import Session
from fastapi import HTTPException

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: SQLModel):
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[SQLModel]:
        try:
            return db.query(self.model).filter(self.model.id == id).first()
        except Exception:
            print(f"{self.model.__name__} with the {id} id not found")

    def get_multi(self, db: Session, *, skip=0, limit=100) -> List[SQLModel]:
        try:
            return db.query(self.model).offset(skip).limit(limit).all()
        except Exception as e:
            print(f"{self.model.__name__} not found")
            print(e)

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> Optional[SQLModel]:
        try:
            db_model = self.model(**obj_in.dict())
            db.add(db_model)
            db.commit()
            db.refresh(db_model)
            return db_model
        except Exception as e:
            print(f"{self.model.__name__} not created")
            print(e)

    def create_multiple(
        self, db: Session, *, obj_in: List[CreateSchemaType]
    ) -> List[SQLModel]:
        try:
            db_models = [self.model(**item.dict()) for item in obj_in]
            db.add_all(db_models)
            db.commit()
            return db_models
        except Exception as e:
            print(f"{self.model.__name__} not created")
            print(e)

    def update(
        self, db: Session, *, id: Any, obj_in: UpdateSchemaType
    ) -> Optional[SQLModel]:
        try:
            db_model = db.get(self.model, id)
            if not db_model:
                raise HTTPException(status_code=404, detail="Hero not found")
            json_data = obj_in.dict(exclude_unset=True)
            for key, value in json_data.items():
                setattr(db_model, key, value)
            db.add(db_model)
            db.commit()
            db.refresh(db_model)
            return db_model

        except Exception as e:
            print(e)

    def delete(self, db: Session, *, id: Any) -> Optional[SQLModel]:
        try:
            db_obj = db.query(self.model).filter(self.model.id == id).first()
            if db_obj is None:
                raise HTTPException(
                    status_code=404, detail=f"{self.model.__name__} not found"
                )
            db.delete(db_obj)
            db.commit()
            return db_obj
        except Exception as e:
            print(f"{self.model.__name__} not deleted")
            print(e)
