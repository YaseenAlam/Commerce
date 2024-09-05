from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import User, Listing, Bid, Comment
from .forms import AuctionListingForm

def index(request):
    listings = Listing.objects.all().values()
    return render(request, "auctions/index.html", {
        "listings": listings,
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


@login_required(login_url="auctions/login.html")
def new_listing(request):
    form = AuctionListingForm(request.POST)
    if form.is_valid():
        auction = Listing(owner=request.user, **form.cleaned_data)
        if not auction.image_url:
            auction.image_url = 'https://us.123rf.com/450wm/jovanas/jovanas1609/jovanas160900216/62250462-no-horse-traffic-sign.jpg?ver=6'
        auction.save()
        starting_bid = auction.starting_bid
        bid = Bid(amount=starting_bid, user=request.user, auction=auction)
        bid.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'auctions/new_listing.html', {
            'form': form,
            'error': form.errors
        })
    

@login_required(login_url="auctions/login.html")
def watchlist(request): 
    return render(request, "auctions/watchlist.html", {
        "listings": request.user.watchlist.all()
    })

@login_required(login_url='auctions/login.html')
def watch(request, id):
    auction = get_object_or_404(Listing, id=id)
    request.user.watchlist.add(auction)
    request.user.watchlist_counter += 1
    request.user.save()
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url='auctions/login.html')
def unwatch(request, id):
    auction = get_object_or_404(Listing, id=id)
    request.user.watchlist.remove(auction)
    request.user.watchlist_counter -= 1
    request.user.save()
    if '/unwatch/' in request.path:
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('wishlist'))

def listing(request, id):
    current = Listing.objects.get(pk=id)
    bid = sorted(get_list_or_404(Bid, auction=current))
    print(bid)
    #comments = Comment.objects.filter(auction=current)
    return render(request, "auctions/listing.html", {
        "listing": current,
        "bid": bid[len(bid) - 1]
    })

def place_bid(request, id):
    if request.method == "POST":
        current = Listing.objects.get(pk=id)
        bidamount = int(request.POST['bid'])
        bidinput = Bid(amount = bidamount, user = request.user, auction = current)
        bidinput.save()
        return render(request, "auctions/result.html", {
            "message": "Succes! Bid has been placed!",
        })