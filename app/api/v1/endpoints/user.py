from fastapi import APIRouter, Header, HTTPException, Depends
from app.mock_data.mock_users import mock_users
from app.exceptions.error_responses import invalid_auth_exception, user_not_found_exception
from app.schemas.user import UsersFindByEmailResponse, UserAddRequest

router = APIRouter()


# 공통 인증 검사 의존성
def verify_token(authorization: str = Header(...)):
    if authorization != "Bearer mock_app_key":
        raise invalid_auth_exception()
    return authorization


@router.get("/users.find_by_email", response_model=UsersFindByEmailResponse)
def find_by_email(email: str, _: str = Depends(verify_token)):
    user = mock_users.get(email)
    if not user:
        raise user_not_found_exception(email)

    return {
        "success": True,
        "user": user
    }


@router.post("/users.add")
def add_user(request: UserAddRequest, authorization: str = Depends(verify_token)):
    if request.email in mock_users:
        raise HTTPException(status_code=409, detail="User already exists.")

    mock_users[request.email] = request.dict()

    return {
        "success": True,
        "message": f"{request.email} added"
    }
