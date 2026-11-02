from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse

from .data import PLAYERS


def hello(request):
    context = {
        "title": "麻將戰績簿",
        "players": PLAYERS,
    }

    return render(request, "core/hello.html", context)


def player_list(request):
    context = {
        "title": "玩家名單",
        "players": PLAYERS,
    }

    return render(request, "core/players.html", context)


def player_detail(request, player_id):
    for player in PLAYERS:
        if player["id"] == player_id:
            context = {
                "title": "玩家個人資料",
                "player": player,
            }

            return render(
                request,
                "core/player_detail.html",
                context,
            )

    raise Http404("找不到這位玩家")


def player_api(request):
    data = {
        "name": "小明",
        "score": 120,
        "status": "active",
    }

    return JsonResponse(
        data,
        json_dumps_params={"ensure_ascii": False}
    )

def players_api(request):
    return JsonResponse(
        PLAYERS,
        safe=False,
        json_dumps_params={"ensure_ascii": False}
    )

def home(request):
    return redirect("hello")


class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "關於本站"
        context["course"] = "PySDV"
        context["player_count"] = len(PLAYERS)

        return context
