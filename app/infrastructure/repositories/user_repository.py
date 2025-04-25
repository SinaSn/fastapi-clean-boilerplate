from typing import Optional

from infrastructure.repositories.base_repository import BaseRepository
from domain.entities.user import User


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db_context.query(User).filter(User.email == email).first()
