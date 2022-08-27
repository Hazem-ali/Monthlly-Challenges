from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    'january': 'Wake up early!',
    'february': 'Read books 10 mins minimum!',
    'march': 'Do some workout!',
    'april': 'Wake up early!',
    'may': 'Read books 10 mins minimum!',
    'june': 'Do some workout!',
    'july': 'Wake up early!',
    'august': 'Read books 10 mins minimum!',
    'september': 'Do some workout!',
    'october': 'Wake up early!',
    'november': 'Read books 10 mins minimum!',
    'december': None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):

    month_names = list(monthly_challenges.keys())

    if month > len(month_names):
        return HttpResponseNotFound("INVALID MONTH NUMBER")

    redirect_month = month_names[month - 1]

    # reverse is used to extract the url using its nickname in views.py
    redirect_path = reverse('monthly-challenge', args=[redirect_month])

    # return HttpResponseRedirect('/challenges/' + redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]

        return render(request, "challenges/challenge.html", {
            'text': challenge_text,
            'month': month
        })
        # render (equals) HttpResponse(render_to_string("challenges/challenge.html"))
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("THIS IS INVALID MONTH")
