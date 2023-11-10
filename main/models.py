# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# # Create your models here.


# class MyAccountManager(BaseUserManager):

#     def create_user(self,first_name,last_name,username,email,password=None):
#         if not email:
#             raise ValueError('user must have an email address')
        
#         if not username:
#             raise ValueError('user must have an username')
        
#         user=self.model(
#             emial=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             last_name=last_name
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
# def create_superuser(self,first_name,last_name,email,username,password):

#         user=self.create_user(
#                 email=self.normalize_email(email),
#                 username=username,
#                 first_name=first_name,
#                 last_name=last_name,
#                 password=password,
#                 )

#         user.is_admin=True
#         user.is_active=True
#         user.is_staff=True
#         user.is_superadmin=True
#         user.save(using=self._db)
#         return user


# class Account(AbstractBaseUser):
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     username=models.CharField(max_length=50,unique=True)
#     email=models.EmailField(max_length=100,unique=True)
#     phone_number=models.CharField(max_length=50)



#     date_joined  =models.DateTimeField(auto_now_add=True)
#     last_login  =models.DateTimeField(auto_now_add=True)
#     is_admin =models.BooleanField(default=False)
#     is_staff =models.BooleanField(default=False)
#     is_active =models.BooleanField(default=False)
#     is_superadmin =models.BooleanField(default=False)



    
#     USERNAME_FIELD ='email'
#     REQUIRED_FIELDS =['username','first_name','last_name']

#     objects=MyAccountManager()

#     def __str__(self):
#         return self.email


#     def  has_perm(self,perm,obj=None):
#         return self.is_admin

#     def has_module_perms(self, add_label):
#         return True


# class PersonalityTypes(models.Model):
#     TypeId = models.CharField(max_length=50)
#     Typename =models.CharField(max_length=100)
#     typeshort_name = models.CharField(max_length=50)
#     TypeDescription = models.CharField(max_length=200)
#     type_image = models.ImageField()

# STATUS=(
#     ('single','never married'),
#     ('divorced','Divorced'),
#     ('widowed','Widowed')
# )
# class UserInformation(models.Model):
#     user = models.OneToOneField("Account", on_delete=models.CASCADE)
#     gender=models.CharField(max_length=20)
#     dateofbirth=models.DateTimeField()
#     maritalstatus = models.CharField(max_length=50, choices=STATUS, default='new')
#     mobile_number=models.IntegerField()
#     #family details
#     father_name=models.CharField(max_length=100)
#     mother_name=models.CharField(max_length=100)
#     NoOfSiblings=models.CharField(max_length=200)

#     #Educational Background:
#     highest_qualification=models.CharField(max_length=100)
#     stream=models.CharField(max_length=50)
#     Institutions_name=models.CharField(max_length=50)
#     yearofpassout=models.DateField()
#     profession=models.CharField(max_length=50)
    
#     Current_Employment_Status=models.BooleanField(default=False)
#     Annual_Income=models.IntegerField()
    
    
#     #Physical Attributes:

#     Height=models.FloatField()
#     Complexion=models.CharField(max_length=100)
#     Body_Type=models.CharField(max_length=100)
#     Hobbies=models.CharField(max_length=100)
#     Interests=models.CharField(max_length=100)

#     #Favorite Activities
#     Lifestyle=models.CharField(max_length=100)
#     Habits=models.TextField(max_length=100)

#     Diet=models.CharField(max_length=100)
    
#     Smoking_Habits=models.BooleanField(default=False)
#     Drinking_Habits=models.BooleanField(default=False)
#     Horoscope=models.TextField()
    
#     #
#     Birth_Star=models.CharField(max_length=100)

#     Raasi=models.CharField(max_length=100)
#     Time_of_Birth=models.DateTimeField()
#     Place_of_Birth=models.CharField(max_length=50)
#     About=models.TextField()

#     #Partner Preferences:

#     Desired_partnerage=models.IntegerField()
#     Preferred_educational_qualifications=models.CharField(max_length=100)
#     partner_profession=models.CharField(max_length=50)
#     partner_preference=models.TextField()

#     Photographs=models.ImageField(upload_to='')

#     quality_photograph=models.ImageField(upload_to='')









#     address_line_1 = models.CharField(blank=True, max_length=50)
#     address_line_2 = models.CharField(blank=True, max_length=50)
#     profile_picture = models.ImageField(blank=True,upload_to='')
#     city = models.CharField(blank=True, max_length=50)
#     state = models.CharField(blank=True, max_length=50)

#     country = models.CharField(blank=True, max_length=50)

#     def __str__(self):
#         return self.user.first_name

#     def full_address(self):
#         return f'{self.address_line_1}{self.address_line_2}'

#     def full_name(self):
#         return f'{self.first_name}{self.last_name}'