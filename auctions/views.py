from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Auction, Comment, Bid


def index(request):
    # Fetch all active auctions from the database
    auctions = Auction.objects.filter(is_active=True)
    # Render the index page with the list of auctions
    return render(request, "auctions/index.html", {
        "auctions": auctions
    })
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def display_auction(request, auction_id):
    # Fetch the auction details from the database
    auction = Auction.objects.get(id=auction_id)
    
    # Fetch bids related to the auction
    bids = Bid.objects.filter(auction=auction)
    
    # Fetch comments related to the auction
    comments = Comment.objects.filter(auction=auction)
    
    # Render the auction details page
    return render(request, "auctions/displayAuctionItem.html", {
        "auction": auction,
        "bids": bids,
        "comments": comments
    })

@login_required
def create_auctionItem(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        end_time = request.POST["end_time"]

        # Create a new auction item
        auction = Auction(
            creator=request.user,
            title=title,
            description=description,
            starting_bid=starting_bid,
            end_time=end_time
        )
        auction.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/createAuctionItem.html")