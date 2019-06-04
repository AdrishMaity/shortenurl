from django.shortcuts import render
from .forms import ShortenURLForm

# Create your views here.
def homePage(request):

    if request.method == 'POST':
        transaction = ShortenURLForm(request.POST)
        if transaction.is_valid():
            print(transaction.cleaned_data)


    transaction = ShortenURLForm()

    context = {
        'result': '',
        'url_form': transaction
    }

    return render(request, "shorturl/home.html", context)
