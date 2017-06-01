from django.shortcuts import render, redirect
import random

def checkPrime(num):
    if num == 1:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def index(request):
    return render(request, 'landscape_app/index.html')

def landscape(request, num):
    num = int(str(num))
    if checkPrime(num):
        randomIndex = random.randint(0, 4)
        list = ['/static/landscape_app/images/farm.jpeg', '/static/landscape_app/images/city.jpg', '/static/landscape_app/images/mountain.jpeg', '/static/landscape_app/images/mountain.jpeg', '/static/landscape_app/images/tree.jpeg']
        src = list[randomIndex]
    elif num <= 10:
        src = '/static/landscape_app/images/city.jpg'
    elif num <= 20:
        src = '/static/landscape_app/images/farm.jpeg'
    elif num <= 30:
        src = '/static/landscape_app/images/mountain.jpeg'
    elif num <= 40:
        src = '/static/landscape_app/images/tree.jpeg'
    elif num <= 50:
        src = '/static/landscape_app/images/water.jpeg'
    else:
        return redirect('/')

    context = {
        'src': src
    }
    return render(request, 'landscape_app/success.html', context)
