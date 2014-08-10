from django.contrib.auth.models import User
from django.db import models
from checkout.models import BaseOrderInfo


class UserProfile(BaseOrderInfo):
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return 'User Profile for: ' + self.user.username

