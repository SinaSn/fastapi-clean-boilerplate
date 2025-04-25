from domain.entities.user_profile import UserProfile
from infrastructure.repositories.base_repository import BaseRepository


class UserProfileRepository(BaseRepository[UserProfile]):
    def __init__(self):
        super().__init__()
