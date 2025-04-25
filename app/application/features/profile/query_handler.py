from fastapi import status

from application.response import Response
from infrastructure.repositories import UserRepository, UserProfileRepository
from domain.schemas.user import UserRead


class ProfileQueryHandler:
    def __init__(self):
        self.user_repository = UserRepository()
        self.user_profile_repository = UserProfileRepository()

    def profile(self, user: dict) -> Response[UserRead]:
        user = self.user_repository.get_by_email(user["email"])
        return Response(
            status_code=status.HTTP_200_OK,
            message="SUCCESSFUL",
            data=UserRead(id=user.id, email=user.email, username=user.username),
        )
