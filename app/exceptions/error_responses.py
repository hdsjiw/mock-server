# error_responses.py

from fastapi import HTTPException


def invalid_auth_exception() -> HTTPException:
    return HTTPException(
        status_code=401,
        detail={
            "success": False,
            "error": {
                "code": "invalid_authentication",
                "message": "Invalid token"
            }
        }
    )


def user_not_found_exception(email: str) -> HTTPException:
    return HTTPException(
        status_code=404,
        detail={
            "success": False,
            "error": {
                "code": "user_not_found",
                "message": f"User '{email}' not found"
            }
        }
    )


def internal_server_error(message: str = "Internal server error") -> HTTPException:
    return HTTPException(
        status_code=500,
        detail={
            "success": False,
            "error": {
                "code": "internal_error",
                "message": message
            }
        }
    )
