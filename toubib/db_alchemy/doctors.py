from typing import Any, Dict, List

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from toubib.api.v1 import schema
from toubib.db import model, pagination
from toubib.utils import logger


class CRUD_Doctors:
    def create_doctor(self, doctor: schema.Doctor, db: Session) -> Any:
        """Add a new doctor record"""
        try:
            db_doctor = model.Doctor(
                first_name=doctor.first_name,
                last_name=doctor.last_name,
                hiring_date=doctor.hiring_date,
                specialization=doctor.specialization,
            )
            db.add(db_doctor)
            db.commit()
            db.refresh(db_doctor)
            return db_doctor
        except SQLAlchemyError as e:
            logger.info(
                f"SQL Alchemy exception has occured while creating a new doctor - {e}"
            )
            return None

    def get_doctor_by_id(self, id: int, db: Session) -> Dict[schema.Doctor]:
        """Get a doctor record by id"""
        try:
            doctor = db.query(model.Doctor).filter(model.Doctor.id == id).first()
            return doctor
        except SQLAlchemyError as e:
            logger.info(
                f"SQL Alchemy exception has occured while reading a doctor record by id - {e}"
            )
            return {}

    def get_all_doctors_by_last_name(
        self, total_pages: int, page_number: int, db: Session
    ) -> List[schema.Doctor]:
        # offset: int, total_items: int,
        """List doctor records alphabetically by last name and by pages of 10 records at a time"""
        try:
            query = db.query(model.Doctor).order_by(model.Doctor.last_name.asc())
            data = pagination.paginate(
                query=query, page=page_number, page_size=total_pages
            )
            return data
        except SQLAlchemyError as e:
            logger.info(
                f"SQL Alchemy exception has occured while listing a doctor record by last_name - {e}"
            )
            return []


crud_doctors = CRUD_Doctors()
