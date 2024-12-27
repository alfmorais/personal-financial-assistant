from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql import or_
from sqlmodel import Session, select

from src.app.user_management.models import User, UserBase


class UserRepository:
    def __init__(self, model: User = User) -> None:
        self.model = model

    def create_user(self, user: UserBase, session: Session) -> User:
        new_user = self.model(**user.model_dump())
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

    def retrieve_by_full_name(self, full_name: str, session: Session) -> User:
        statement = select(self.model).where(
            self.model.full_name == full_name,
        )

        try:
            user = session.exec(statement).one()
        except NoResultFound:
            session.rollback()
            return None

        return user

    def retrieve_by_username(self, username: str, session: Session) -> User:
        statement = select(self.model).where(
            self.model.username == username,
        )

        try:
            user = session.exec(statement).one()
        except NoResultFound:
            session.rollback()
            return None

        return user

    def retrieve_by_email(self, email: str, session: Session) -> User:
        statement = select(self.model).where(self.model.email == email)

        try:
            user = session.exec(statement).one()
        except NoResultFound:
            session.rollback()
            return None

        return user

    def retrieve_by_username_and_email(
        self,
        user: UserBase,
        session: Session,
    ) -> User:
        statement = select(self.model).where(
            or_(
                self.model.username == user.username,
                self.model.email == user.email,
            )
        )
        has_an_user = session.exec(statement).fetchall()
        return has_an_user

    def delete_user(self, username: str, session: Session) -> None:
        statement = select(self.model).where(
            self.model.username == username,
        )
        user = session.exec(statement).one()
        session.delete(user)
        session.commit()

    def updade_full_name(
        self,
        full_name: str,
        new_full_name: str,
        session: Session,
    ) -> User:
        statement = select(self.model).where(
            self.model.full_name == full_name,
        )
        user = session.exec(statement).one()
        user.full_name = new_full_name
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def updade_username(
        self,
        username: str,
        new_username: str,
        session: Session,
    ) -> User:
        statement = select(self.model).where(self.model.username == username)
        user = session.exec(statement).one()
        user.username = new_username
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def updade_email(
        self,
        email: str,
        new_email: str,
        session: Session,
    ) -> User:
        statement = select(self.model).where(self.model.email == email)
        user = session.exec(statement).one()
        user.email = new_email
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def updade_password(
        self,
        password: str,
        new_password: str,
        session: Session,
    ) -> User:
        statement = select(self.model).where(self.model.password == password)
        user = session.exec(statement).one()
        user.password = new_password
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


user_repository = UserRepository()
