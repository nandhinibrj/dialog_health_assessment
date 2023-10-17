from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .db import db_session
from toubib.api.v1 import schema
from toubib.db import database
from toubib.db_alchemy import crud_patients
from toubib.utils import api_response_code, response

router = APIRouter()

@router.post(
    "/", responses=response.general_responses, status_code=status.HTTP_201_CREATED
)
async def create_patient(
        patient: schema.Patient
) -> JSONResponse:
    """Create a new patient record"""
    data = crud_patients.create_patient(patient=patient, db=next(database.get_session()))
    if data is None:
        return JSONResponse(api_response_code.response_500(data))
    return JSONResponse(api_response_code.response_201(data))


@router.get(
    "/{patient_id}", responses=response.get_patients_response, status_code=status.HTTP_200_OK
)
def get_patient_by_id(
        patient_id: int
) -> JSONResponse:
    """Read a patient record by id"""
    if patient_id is not None:
        data = crud_patients.get_patient_by_id(id=patient_id, db=next(database.get_session()))
        if data is None:
            return JSONResponse(api_response_code.response_500())
        else:
            json_encoded_data = jsonable_encoder(data)
            return JSONResponse(status_code=200, content=json_encoded_data)


@router.get(
    "/", responses=response.list_patients_responses, status_code=status.HTTP_200_OK
)
def list_patients_by_last_name(
        offset: int,
        total_pages: int,
        page_number: int,
        total_items: int,
) -> JSONResponse:
    """List patients by pages"""
    data = crud_patients.get_all_patients_by_last_name(
        total_pages=total_pages, page_number=page_number,  db=next(database.get_session())
    )
    if data is None:
        return JSONResponse(api_response_code.response_500(data))
    json_encoded_data = jsonable_encoder(data)
    return JSONResponse(
        status_code=200,
        content={
            "data": json_encoded_data,
            "meta": {
                "offset": offset,
                "total_items": total_items,
                "total_pages": total_pages,
                "page_number": page_number,
            },
        },
    )
