from fastapi import APIRouter, HTTPException, Depends, status
from typing import Any

from core.security import get_current_user
from domain.schemas.user import UserRead
from application.features.profile.query_handler import ProfileQueryHandler

router = APIRouter()

profile_query_handler = ProfileQueryHandler()


@router.get("", response_model=UserRead)
def get_profile(user: dict = Depends(get_current_user)):
    result = profile_query_handler.profile(user)
    if result.status_code == status.HTTP_200_OK:
        return result.data
    return HTTPException(status_code=result.status_code, detail=result.message)
