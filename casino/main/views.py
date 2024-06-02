from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def auth(request):
    return render(request, 'main/signup.html')


def nepoker(request):
    return render(request, 'main/nepoker.html')


def TwentyOne(request):
    return render(request, 'main/TwentyOne.html')

def roulette(request):
    return render(request, 'main/roulette.html')



