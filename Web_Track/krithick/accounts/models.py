from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, phone, adhar, password):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        if not phone:
            raise ValueError("Users must have an phone number")
        if not adhar:
            raise ValueError("Users must have an adhar number")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            phone = phone,
            adhar = adhar,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, adhar, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            phone = phone,
            adhar = adhar,
            password = password
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser):
    email = models.EmailField(unique=True)

    username = models.CharField(max_length=150, unique=True)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    phone = models.IntegerField(verbose_name='phone number')
    adhar = models.IntegerField(verbose_name='adhar number', unique=True)

    USERNAME_FIELD = 'email' # this should be used to login
    REQUIRED_FIELDS = ['username', 'phone', 'adhar']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
