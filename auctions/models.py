from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction():
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=240)
    category = models.CharField(max_length=64)
    url = models.CharField(max_length=240)
    bid = models.FloatField()

    def __str__(self):
        return f"{self.title}"

class Bid():
    pass

class Comment():
    pass

# auction 
# listings
# bids
# comments made on auction listings