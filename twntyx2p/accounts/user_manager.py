from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, phone):
        """
        Creates and saves a User with the given email and password.
        """
        if not email or phone:
            raise ValueError('Users must have an email address or phone')
        else:
            if email:
                user = self.model(
                    email=self.normalize_email(email),
                )
            if phone:
                user.phone = phone

        user.set_password(password)

        user.save(using=self._db)
        return user
