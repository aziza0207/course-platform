import pytest

from django.contrib.auth import get_user_model


@pytest.mark.django_db
class TestModel:
    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        assert user.email == email
        assert user.check_password(password)

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']

        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            assert user.email == expected

    def test_create_superuser(self):
        email = 'test123@example.com'
        password = 'test123'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        assert user.is_superuser
        assert user.is_staff

    def test_create_mentor(self):
        email = 'test1234@example.com'
        password = 'test1234'
        user = get_user_model().objects.create_mentor(
            email=email,
            password=password
        )
        assert user.is_staff
        assert user.is_mentor
