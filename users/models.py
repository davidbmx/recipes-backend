import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.main_model import MainModel

def upload_image(instance, filename):
    return f'users/{instance.user.username}/{filename}'

class User(MainModel, AbstractUser):
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'Email is already regitered'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    uid = models.TextField(db_index=True, default=uuid.uuid4)

    following = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to=upload_image, blank=True, null=True)

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username
    
class Follow(MainModel):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_followers')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_following')

    def __str__(self):
        return f"{self.follower.username} following: {self.following.username}"
    