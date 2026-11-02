from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/", views.hello, name="hello"),
    path("players/", views.player_list, name="players"),
    path("players/<int:player_id>/", views.player_detail, name="player_detail"),
    path("api/player/", views.player_api, name="player_api"),
    path("api/players/", views.players_api, name="players_api"),
    path("about/", views.AboutView.as_view(), name="about"),
]
