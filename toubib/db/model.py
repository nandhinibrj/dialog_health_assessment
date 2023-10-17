import uuid
from datetime import datetime

from toubib.db.database import base
from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    UniqueConstraint,
)


class Patient(base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    date_of_birth = Column(String, nullable=False)
    sex_at_birth = Column(String, nullable=False)
    # created_timestamp = Column(TIMESTAMP, nullable=False, default=datetime.now())
    # modified_timestamp = Column(TIMESTAMP, nullable=False, default=datetime.now())

    __table_args__ = (
        PrimaryKeyConstraint("id", name="patient_primary_key_id"),
        UniqueConstraint("email"),
        # {"schema": "patient", "extend_existing": True},
    )

    def __repr__(self):
        return (
            f"Patient('{self.id}','{self.first_name}'"
            f",'{self.first_name}'"
            f",'{self.last_name}'"
            f",'{self.email}'"
            f",'{self.date_of_birth}'"
            f",'{self.sex_at_birth}'"
            # f",'{self.created_timestamp}'"
            # f",'{self.modified_timestamp}')"
        )


class Doctor(base):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, index=True, default=uuid.uuid4())
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    hiring_date = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    modified_at = Column(TIMESTAMP, nullable=False, default=datetime.now())

    __table_args__ = (
        PrimaryKeyConstraint("id", name="doctor_primary_key_id"),
        {"schema": "doctor", "extend_existing": True},
    )

    def __repr__(self):
        return (
            f"Doctor('{self.id}','{self.first_name}'"
            f",'{self.first_name}'"
            f",'{self.last_name}'"
            f",'{self.hiring_date}'"
            f",'{self.specialization}'"
            f",'{self.created_at}'"
            f",'{self.modified_at}')"
        )
