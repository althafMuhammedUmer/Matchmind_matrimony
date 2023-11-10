from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        
        user = self.model(
            username=username,
            email=self.normalize_email(email), 
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True


        user.save(using=self._db)
        return user
    
class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55, blank=True)
    email = models.EmailField(max_length=55, unique=True)
    username = models.CharField(max_length=55, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, null=True, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_admin =models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, add_label):
        return True
