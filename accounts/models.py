from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

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
                password = password,
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

class User(AbstractBaseUser):
    #fields what user enter
    email               = models.EmailField(verbose_name='email', max_length=100, unique=True)
    username            = models.CharField(max_length = 30, unique=True)

    # the real name what use to create auto email form
    first_name          = models.CharField(max_length = 30)
    last_name           = models.CharField(max_length = 30)

    # the name what display when user create blog or comment
    display_name        = models.CharField(max_length = 50)



    #auto set
    date_joined         = models.DateTimeField(verbose_name='date jointed', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    # setup
    #_________________________________________________________________________

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
            'email',
            'first_name',
            'last_name'
        ]

    objects = AccountsManage()

    def __str__(self):
        return self.username

    def  has_perm(self,perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True