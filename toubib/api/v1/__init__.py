from fastapi import APIRouter

from toubib.api.v1.routes import patient

api_version_v1 = APIRouter()

api_version_v1.include_router(patient.router, tags=["patient", "doctor"], prefix="/patients")
