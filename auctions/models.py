from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlist_counter = models.IntegerField(default=0, blank=True)
    watchlist = models.ManyToManyField("Listing", related_name="watchlist", blank=True)
    pass


class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=12, decimal_places=2)
    image_url = models.ImageField(blank=True, null=True)
    category = models.CharField(max_length=65, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    winner = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.title} by {self.owner.username}'



class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount} on {self.auction} by {self.user.username}'

class Comment():
    pass

