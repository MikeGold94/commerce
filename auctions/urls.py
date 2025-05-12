from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_auctionItem", views.create_auctionItem, name="create_auctionItem"),
    path("auction/<int:auction_id>", views.display_auction, name="display_auction")
]
