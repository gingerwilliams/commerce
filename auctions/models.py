from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Now


class User(AbstractUser):
    pass

# class Auction():
#     pass
 
class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=240)
    category = models.CharField(max_length=64)
    url = models.CharField(max_length=240)
    bid = models.FloatField()

    def __str__(self):
        return f"{self.title} - {self.bid}"

class Bid():
    # listing key
    pass


class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    comment = models.CharField(max_length=260)
    date = models.DateTimeField(db_default=Now())

    def __str__(self):
        return f"{self.user} - {self.date}"
