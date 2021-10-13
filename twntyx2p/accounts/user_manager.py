from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        print(email+":"+password)
        if not email:
            raise ValueError('Users must have an email address')
        else:
            user = self.model(
                email=self.normalize_email(email),
            )

        user.set_password(password)

        return user
