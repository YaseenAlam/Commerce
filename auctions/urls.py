from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watch/<int:id>", views.watch, name="watch"),
    path("unwatch/<int:id>", views.unwatch, name="unwatch"),
    path("listing/<int:id>", views.listing, name="listing" ),
    path("place_bid/<int:id>", views.place_bid, name="place_bid")
]
