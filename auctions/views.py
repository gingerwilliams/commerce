from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.timezone import now as Now
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Comment, Bid


def index(request, ):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


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

def listing(request, id):
    listing = Listing.objects.get(pk=id)
    comments = Comment.objects.filter(listing=listing)
    bid = Bid.objects.filter(listing=listing)
    max_bid = bid[len(bid) -1]

    if request.method == 'POST':
        comment = request.POST['comment']

        if request.user.is_authenticated:
            user = request.user
            new_comment = Comment(comment=comment, listing=listing, user=user, date=Now())
            new_comment.save()

    return render(request, "auctions/listing.html" 
        ,{
            "title": listing.title,
            "description": listing.description,
            "url": listing.url,
            "comments": comments,
            "bid": max_bid.bid,
            "id": id
        }
    )

def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        url = request.POST['url']
        bid = request.POST['bid']

        new_listing = Listing(
            title=title,
            description=description,
            url=url,
            bid=bid
        )
        new_listing.save()

        print(title)
    return render(request, "auctions/new.html")