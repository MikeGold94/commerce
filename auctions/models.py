from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """
    # Add any additional fields you want to include in your custom user model
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    Watchlist = models.ManyToManyField('Auction', through='Watchlist', related_name='watchers')
    password = models.CharField(max_length=128)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.username

class Auction(models.Model):
    """
    Model representing an auction.
    """
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctions')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='auctions', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
class Bid(models.Model):
    """
    Model representing a bid on an auction.
    """
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"
class Watchlist(models.Model):
    """
    Model representing a user's watchlist for auctions.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlists')
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='watchlists')

    def __str__(self):
        return f"{self.user.username} - {self.auction.title}"
class Comment(models.Model):
    """
    Model representing a comment on an auction.
    """
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content}"
class Category(models.Model):
    """
    Model representing a category for auctions.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
class AuctionCategory(models.Model):
    """
    Model representing the many-to-many relationship between auctions and categories.
    """
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.auction.title} - {self.category.name}"

