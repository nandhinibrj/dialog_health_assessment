response_codes = {
    400: {"description": "Bad Request"},
    401: {"description": "Unauthorized"},
    404: {"description": "Not Found"},
    422: {"description": "Validation Error"},
    500: {"description": "Internal Server Error"},
}

general_responses = {
    **response_codes,
    200: {
        "content": {"application/json": {"example": {"message": "success"}}},
    },
}

list_patients_responses = {
    **response_codes,
    200: {
        "content": {
            "application/json": {
                    "data": [
                        {
                            "id": 17,
                            "email": "mulatu@astatke",
                            "first_name": "Mulatu",
                            "last_name": "Astatke",
                            "date_of_birth": "1943-12-19",
                            "sex_at_birth": "MALE",
                        },
                        {
                            "id": 21,
                            "email": "tracy@edwards.com",
                            "first_name": "Tracy",
                            "last_name": "Edwards",
                            "date_of_birth": "1962-09-05",
                            "sex_at_birth": "FEMALE",
                        },
                    ],
                    "meta": {
                        "offset": 40,
                        "total_items": 42,
                        "total_pages": 5,
                        "page_number": 5,
                    },
            }
        }
    },
}

get_patients_response = {
    **response_codes,
    200: {
        "content": {
            "application/json": {
                "data": {
                    "id": 1,
                    "email": "tracy@edwards.com",
                    "first_name": "Tracy",
                    "last_name": "Edwards",
                    "date_of_birth": "1962-09-05",
                    "sex_at_birth": "FEMALE",
                }
            },
        }
    },
}

get_doctors_response = {
    **response_codes,
    200: {
        "content": {
            "application/json": {
                "data": {
                    "id": 1,
                    "first_name": "Tracy",
                    "last_name": "Edwards",
                    "hiring_date": "1962-09-05",
                    "specialization": "Gynecologist",
                }
            },
        }
    },
}

list_doctors_responses = {
    **response_codes,
    200: {
        "content": {
            "application/json": {
                    "data": [
                        {
                            "id": 17,
                            "first_name": "Mulatu",
                            "last_name": "Astatke",
                            "hiring_date": "1962-09-05",
                            "specialization": "Gynecologist",
                        },
                        {
                            "id": 21,
                            "first_name": "Tracy",
                            "last_name": "Edwards",
                            "hiring_date": "1962-09-05",
                            "specialization": "Orthopedic",
                        },
                    ],
                    "meta": {
                        "offset": 40,
                        "total_items": 42,
                        "total_pages": 5,
                        "page_number": 5,
                    },
            }
        }
    },
}
