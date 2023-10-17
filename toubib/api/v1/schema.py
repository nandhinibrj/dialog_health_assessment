from pydantic import BaseModel


class PatientBase(BaseModel):
    email: str = None
    first_name: str = None
    last_name: str = None
    date_of_birth: str = None
    sex_at_birth: str = None


class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True


class DoctorBase(BaseModel):
    first_name: str = None
    last_name: str = None
    hiring_date: str = None
    specialization: str = None


class Doctor(DoctorBase):
    id: int

    class Config:
        orm_mode = True
