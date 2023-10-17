from typing import Union

from fastapi import status
from fastapi.responses import JSONResponse, ORJSONResponse, Response


def response_200(
    data: Union[dict, list] = None, *, message: str = "Success"
) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"code": 200, "message": message, "data": data},
    )


def response_201(
    data: Union[dict] = None, *, message: str = "Created Record Successfully"
) -> Response:
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"code": 201, "message": message, "data": data},
    )


def response_403(data: str = None) -> Response:
    return ORJSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={"code": 403, "message": "403 - Forbidden", "data": data},
    )


def response_404(data: str = None) -> Response:
    return ORJSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"code": 404, "message": "404 - Not Found", "data": data},
    )


def response_405(data: str = None) -> Response:
    return ORJSONResponse(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        content={"code": 405, "message": "405 - Method Not Allowed", "data": data},
    )


def response_401(data: str = None) -> Response:
    return ORJSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"code": 401, "message": "401 - Unauthorized", "data": data},
    )


def response_400(data: str = None) -> Response:
    return ORJSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"code": 400, "message": "400 - Bad Request", "data": data},
    )


def response_500(data: str = None) -> Response:
    return ORJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"code": 500, "message": "500 - Internal Server Error", "data": data},
    )
