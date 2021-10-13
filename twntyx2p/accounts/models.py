from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from twntyx2p.accounts.user_manager import UserManager


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone = models.CharField(max_length=12, unique=True, null=True)
    phone_code = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False)
    realm_name = models.CharField(unique=True, null=False, max_length=16)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    created_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def get_email(self):
        # The user is identified by their email address
        return self.email

    def get_realm_name(self):
        # The user is identified by their email address
        return self.realm_name

    def __str__(self):
        return self.email

    def save_sms_code(self, code):
        self.phone_code = code

    def activate(self, user_code):
        if user_code == self.phone_code:
            self.is_active = True
        return self.is_active

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
