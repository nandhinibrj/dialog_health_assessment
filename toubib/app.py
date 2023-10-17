import traceback

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from toubib.db.database import SessionLocal
from utils import logger

from toubib.api.v1 import api_version_v1
from toubib.config.config import APPSettings
from toubib.utils import (
    response_400,
    response_401,
    response_403,
    response_404,
    response_405,
    response_500,
)


def create_app():
    # Add FAST API settings
    app = FastAPI(
        title=APPSettings.APP_NAME,
        description=APPSettings.APP_DESCRIPTION,
        version=APPSettings.APP_VERSION,
        docs_url=f"{APPSettings.APP_VERSION_PATH}/docs",
    )
    # Add CORS Settings
    app.add_middleware(CORSMiddleware,
                       allow_origins=APPSettings.APP_CORS_ORIGIN,
                       allow_credentials=True,
                       allow_methods=APPSettings.APP_CORS_ALLOWED_METHODS,
                       allow_headers=APPSettings.APP_CORS_ALLOWED_HEADERS)
    # call API Routers from v1
    app.include_router(api_version_v1, prefix=APPSettings.APP_VERSION_PATH)
    middlerware_set_up(app)
    handle_exception(app)
    return app


def set_logger(request: Request):
    logger.info(
        f'Medical Records API-{request.method}-url:{request.url}-\nclient_host:{request.client.host}-client_port:{request.client.port}-\nheaders:{request.headers.get("user-agent")}\n-traceback:{traceback.format_exc()}'
    )

def middlerware_set_up(app: FastAPI):
    @app.middleware("http")
    async def log_set_up(request: Request, call_next):
        set_logger(request)
        response = await call_next(request)
        return response

def handle_exception(app: FastAPI):
    # @app.exception_handlers(RequestValidationError)
    async def bad_request_exception(request: Request):
        set_logger(request)
        return response_400()

    # @app.exception_handlers(Exception)
    async def all_exception(request: Request):
        set_logger(request)
        return response_500()

    # @app.exception_handlers(Exception)
    async def forbidden_exception(request: Request):
        set_logger(request)
        return response_403()

    # @app.exception_handlers(Exception)
    async def not_found_exception(request: Request):
        set_logger(request)
        return response_404()

    # @app.exception_handlers(Exception)
    async def cor_method_exception(request: Request):
        set_logger(request)
        return response_405()

    # @app.exception_handlers(Exception)
    async def unauthorized_exception(request: Request):
        set_logger(request)
        return response_401()
