from typing import Any, Dict, List
from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from toubib.api.v1 import schema
from toubib.db import model
from toubib.utils import logger


class CRUD_Patients:

    def create_patient(self, patient: schema.Patient, db: Session) -> Any:
        """Add a new patient record"""
        try:
            print("db-alchemy-create-patients======>>>>", db)
            db_patient = model.Patient(
                first_name=patient.first_name,
                last_name=patient.last_name,
                email=patient.email,
                date_of_birth=patient.date_of_birth,
                sex_at_birth=patient.sex_at_birth,
            )
            print("db_patient-read-here", db_patient)
            db.add(db_patient)
            db.commit()
            db.refresh(db_patient)

            return db_patient
        except SQLAlchemyError as e:
            logger.info(
                f"SQL Alchemy exception has occured while creating a new patient - {e}"
            )
            return None

    def get_patient_by_id(self, id: int, db: Session) -> Any:
        """Get a patient record by id"""
        try:
            patient = db.query(model.Patient).get(id)
            print("what happened here====>>", id)
            return patient
        except SQLAlchemyError as e:
            logger.info(
                f"SQL Alchemy exception has occured while reading a patient record by id - {e}"
            )
            return None

    def get_all_patients_by_last_name(
            self, total_pages: int, page_number: int, db: Session
    ) -> Any:
        # offset: int, total_items: int,
        """List patient records alphabetically by last name and by pages of 10 records at a time"""
        try:
            query = db.query(model.Patient).order_by(model.Patient.last_name.asc())
            if page_number <= 0:
                raise AttributeError("Page needs to be greater than 1")
            if total_pages <= 0:
                raise AttributeError("Page size needs to be greater than 1")
            records = query.limit(total_pages).offset((page_number - 1) * total_pages).all()
            total = query.count()
            return records
        except SQLAlchemyError as e:
            logger.info(
                f"SQL Alchemy exception has occured while listing a patient record by last_name - {e}"
            )
            return None


crud_patients = CRUD_Patients()
