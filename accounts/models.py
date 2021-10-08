from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
'''
class AccountsManage(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password = None):
        if not email:
            raise ValueError("User must have email address!")
        if not username:
            raise ValueError("User must have username!")
        if not first_name or not last_name:
            raise ValueError("You need to complate your profile!")

        user = self.model(
                email = self.normalize_email(email),
                username = username,
                first_name = first_name,
                last_name = last_name
            )
        
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(
                email = self.normalize_email(email),
                username = username,
                password = password,
                first_name= first_name,
                last_name = last_name
            )
        user.is_admin =True
        user.is_staff =True
        user.is_superuser =True
        user.save(using = self._db)
        return user
'''
class User(AbstractUser):
    display_name = models.CharField(max_length= 60)

    REQUIRED_FIELDS =['email', 'first_name', 'last_name']


    def __str__(self):
        return super().__str__()
    