from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for entire month!",
    "february": "Walk for at least 30 minutes daily!",
    "march": "Learn Django for at least 20 minutes daily!",
    "april": "Eat no meat for entire month!",
    "may": "Walk for at least 30 minutes daily!",
    "june": "Learn Django for at least 20 minutes daily!",
    "july": "Eat no meat for entire month!",
    "august": "Walk for at least 30 minutes daily!",
    "september": "Learn Django for at least 20 minutes daily!",
    "october": "Eat no meat for entire month!",
    "november": "Walk for at least 30 minutes daily!",
    "december": None
}

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for entire month!")

# def february(request):
#     return HttpResponse("Walk for at least 30 minutes daily!")


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except (IndexError, ValueError):
        return HttpResponseNotFound("Invalid month number!")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"month": month, "challenge": challenge_text})
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # raise Http404()
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
