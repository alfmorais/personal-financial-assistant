from fastapi import HTTPException, status
from sqlmodel import Session

from .models import User
from .repositories import UserRepository, user_repository


class UserService:
    def __init__(self, repository: UserRepository = user_repository):
        self.repository = repository

    def create_user(self, user, session) -> User:
        users = self.repository.retrieve_by_username_and_email(
            user,
            session,
        )

        if users:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with username or email already exist.",
            )

        new_user = self.repository.create_user(user, session)
        return new_user

    def retrieve_user_by_username(
        self,
        username: str,
        session: Session,
    ) -> User:
        user = self.repository.retrieve_by_username(
            username,
            session,
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Username: {username} does not exist.",
            )

        return user

    def delete_user(self, username: str, session: Session) -> None:
        user = self.repository.retrieve_by_username(
            username,
            session,
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Username: {username} does not exist.",
            )

        self.repository.delete_user(username, session)

    def updade_full_name(self, username: str, session: Session): ...

    def updade_username(self): ...
    def updade_email(self): ...
    def updade_password(self): ...


user_service = UserService()
