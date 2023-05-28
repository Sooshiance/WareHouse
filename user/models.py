from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class AllUser(BaseUserManager):
    def create_user(self, email, username, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        
        if not username:
            raise ValueError("'Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **kwargs,
        )
        user.is_active  = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, username, email, password):
        user = self.create_user(
            email=email,
            password=password,
            username=username,
        )
        user.is_staff = True
        user.is_active  = False
        user.is_superuser = False        
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=email,
            password=password,
            username=username,
        )
        user.is_staff = True
        user.is_active  = True
        user.is_superuser = True        
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')
    numbers     = RegexValidator(r'^[0-9a]*$', message='Only numbers are allowed.')
    
    # Required fields for UserAccount model
    
    username    = models.CharField(unique=True, max_length=150, validators=[alphanumeric])
    email       = models.EmailField(unique=True, max_length=244)
    
    # You can add up your fields based on your project definition
    
    first_name  = models.CharField(max_length=75, null=True, blank=True, validators=[alphanumeric])
    last_name   = models.CharField(max_length=75, null=True, blank=True, validators=[alphanumeric])
    phone       = models.CharField(max_length=12, null=True, blank=True, validators=[numbers])
    pic         = models.ImageField(upload_to="user/")
    description = models.TextField(max_length=1024, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    # Required fields for AllUser model 
    
    is_active   = models.BooleanField(default=False, null=False)
    is_staff    = models.BooleanField(default=False, null=False)
    is_superuser= models.BooleanField(default=False, null=False)

    objects = AllUser()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        fullname = self.first_name+" "+self.last_name
        return fullname

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        # Simplest possible answer: Yes, always
        return True
    
    class Meta:
        ordering = ["-created_at"]


class UserProfile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name="userprofile")
    email = models.EmailField()
    username = models.CharField(max_length=150)
    
    # You can add or remove any field from UserAccount model 
    
    first_name  = models.CharField(max_length=75, null=True, blank=True)
    last_name   = models.CharField(max_length=75, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} {self.email} {self.created_at}"
    
    class Meta:
        ordering = ["-created_at"]
