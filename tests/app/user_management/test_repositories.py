import pytest

from src.app.user_management.models import UserBase
from src.app.user_management.repositories import user_repository


class TestUserRepository:
    @pytest.fixture
    def user_data(self):
        return UserBase(
            username="testuser",
            email="testuser@example.com",
            full_name="Test User",
            password="password123",
        )

    def test_create_user(self, session, user_data):
        user = user_repository.create_user(user_data, session)

        assert user.username == user_data.username
        assert user.email == user_data.email
        assert user.full_name == user_data.full_name

    def test_retrieve_by_username(self, session, user_data):
        user_repository.create_user(user_data, session)
        user = user_repository.retrieve_by_username(
            user_data.username,
            session,
        )

        assert user is not None
        assert user.username == user_data.username

    def test_retrieve_by_email(self, session, user_data):
        user_repository.create_user(user_data, session)
        user = user_repository.retrieve_by_email(
            user_data.email,
            session,
        )

        assert user is not None
        assert user.email == user_data.email

    def test_retrieve_by_full_name(self, session, user_data):
        user_repository.create_user(user_data, session)
        user = user_repository.retrieve_by_full_name(
            user_data.full_name,
            session,
        )

        assert user is not None
        assert user.full_name == user_data.full_name

    def test_retrieve_by_username_and_email(self, session, user_data):
        user_repository.create_user(user_data, session)
        another_user_data = UserBase(
            username="anotheruser",
            email="anotheruser@example.com",
            full_name="Another User",
            password="password456",
        )
        user_repository.create_user(another_user_data, session)

        users = user_repository.retrieve_by_username_and_email(
            user_data,
            session,
        )

        assert len(users) == 1
        assert users[0].username == user_data.username

    def test_delete_user(self, session, user_data):
        user_repository.create_user(user_data, session)
        user_repository.delete_user(user_data.username, session)
        user = user_repository.retrieve_by_username(
            user_data.username,
            session,
        )

        assert user is None

    def test_update_full_name(self, session, user_data):
        user_repository.create_user(user_data, session)
        new_name = "Updated User"
        updated_user = user_repository.updade_full_name(
            user_data.full_name, new_name, session
        )

        assert updated_user.full_name == new_name

    def test_update_username(self, session, user_data):
        user_repository.create_user(user_data, session)
        new_username = "updateduser"
        updated_user = user_repository.updade_username(
            user_data.username, new_username, session
        )

        assert updated_user.username == new_username

    def test_update_email(self, session, user_data):
        user_repository.create_user(user_data, session)
        new_email = "updateduser@example.com"
        updated_user = user_repository.updade_email(
            user_data.email,
            new_email,
            session,
        )

        assert updated_user.email == new_email

    def test_update_password(self, session, user_data):
        user_repository.create_user(user_data, session)
        new_password = "newpassword123"
        updated_user = user_repository.updade_password(
            user_data.password, new_password, session
        )

        assert updated_user.password == new_password
