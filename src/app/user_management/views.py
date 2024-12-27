from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from src.infrastructure.database.utils import get_session

from .models import (
    User,
    UserBase,
    UserEmail,
    UserFullName,
    UserPassword,
    UserUsername,
)
from .services import user_service

router = APIRouter(tags=["Users"])


@router.post(
    "/users",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user: UserBase,
    session: Session = Depends(get_session),
):
    new_user = user_service.create_user(user, session)
    return new_user


@router.get(
    "/users/{username}",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
def retrieve_user_by_username(
    username: str,
    session: Session = Depends(get_session),
):
    user = user_service.retrieve_user_by_username(username, session)
    return user


@router.delete(
    "/users/{username}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(
    username: str,
    session: Session = Depends(get_session),
):
    user_service.delete_user(username, session)


@router.put(
    "/users/{username}/full-name",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
def updade_full_name(
    username: str,
    user: UserFullName,
    session: Session = Depends(get_session),
):
    user = user_service.retrieve_user_by_username(username, session)
    return user


@router.put(
    "/users/{username}/username",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
def updade_username(
    username: str,
    user: UserUsername,
    session: Session = Depends(get_session),
):
    user = user_service.retrieve_user_by_username(username, session)
    return user


@router.put(
    "/users/{username}/email",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
def updade_email(
    username: str,
    user: UserEmail,
    session: Session = Depends(get_session),
):
    user = user_service.retrieve_user_by_username(username, session)
    return user


@router.put(
    "/users/{username}/password",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
def updade_password(
    username: str,
    user: UserPassword,
    session: Session = Depends(get_session),
):
    user = user_service.retrieve_user_by_username(username, session)
    return user
