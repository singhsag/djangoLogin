from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    # here we are not fully inherit from User class insted use;
    user = models.OneToOneField(User, null=True, on_delete = models.SET_NULL)

    # additional
    portfolio_site = models.URLField(blank = True)

    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username
        # where username is the default attribute of user
