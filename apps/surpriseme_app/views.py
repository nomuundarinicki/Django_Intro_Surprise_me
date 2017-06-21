# Create your views here.
from __future__ import unicode_literals
from random import shuffle
from itertools import islice
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'surpriseme_app/index.html')

def guess(request):
    value = ['HI there, Welcome', \
    'How are you liking this surprise?', \
    'Whoooohooo.']
    if request.method == "POST":
        shuffle(value)
        lines = int(request.POST['numoflines'])
        counter = 0
        messages = []
        for element in islice(value, 0, lines):
            messages.append(element)
            counter += 1
        context = {
            "messages": messages
        }
    return render(request, 'surpriseme_app/guess.html', context)
