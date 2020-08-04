from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    role = (
    ('client', 'Клиент'),
    ('REST', 'Ресторан'),
    ('Cour', 'Курьер')
)
    username = None
    email = models.EmailField(_('Email'), unique=True)
    role = models.CharField('Тип записи', max_length=20, choices=role, default='green')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    famil = models.CharField(max_length=20)

class Courier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    famil = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    car = models.BooleanField(default=False)
    
class Rest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    name_res = models.CharField(max_length=20)
    addres = models.CharField(max_length=40)

