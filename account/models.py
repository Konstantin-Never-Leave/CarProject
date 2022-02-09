from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.
    objects = UserManager()

    # should be activated after email confirmation:
    is_active = models.BooleanField(default=True)

    # type selection:
    # user_type = models.ForeignKey(UserType, on_delete=models.PROTECT, verbose_name="Type of user")

    # user attributes:
    username = models.CharField(verbose_name="nickname", max_length=40, unique=True)
    first_name = models.CharField(verbose_name="name", max_length=255)
    second_name = models.CharField(verbose_name="surname", max_length=255)
    preview = models.ImageField(upload_to="logo/%Y/%m/%d", verbose_name="Preview image", )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    time_created = models.DateTimeField(auto_now=True)
    time_updated = models.DateTimeField(auto_now_add=True)
    groups = None
    user_permissions = None

    def get_full_name(self):
        # The user is identified by their email address
        return f"{self.username} {self.email}"

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def get_slug(self):
        return self.username

    slug = models.SlugField(max_length=40, unique=True, db_index=True, verbose_name="User URL",
                            default="username")
