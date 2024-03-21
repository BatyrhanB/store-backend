from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    """

    use_in_migrations = True

    def _create_user(self, email, is_superuser, is_staff, is_active, password=None):
        if not email:
            raise ValueError("User must have an email")
        user = self.model(
            email=email,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None):
        """
        Create a user with the given email and password
        """
        return self._create_user(
            email=email,
            is_superuser=False,
            is_staff=False,
            is_active=True,
            password=password,
        )

    def create_superuser(self, email, password):
        """
        Create superuser with the given email and password
        """
        return self._create_user(
            email=email,
            is_superuser=True,
            is_staff=True,
            is_active=True,
            password=password,
        )
