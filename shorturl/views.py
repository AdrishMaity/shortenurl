from django.shortcuts import render
from .forms import ShortenURLForm
import requests
import json
import urllib
from bs4 import BeautifulSoup
from .models import ShortenURL



# Create your views here.
def homePage(request):

    if request.method == 'POST':
        transaction = ShortenURLForm(request.POST)
        if transaction.is_valid():
            cleaned_data = transaction.cleaned_data
            print(cleaned_data)
            enteredURL = cleaned_data['url']

            try:
                soup = BeautifulSoup(urllib.request.urlopen(cleaned_data['url']))

            except urllib.error.URLError as e:
                print(e.reason)
                error = e.reason
                result_data = ''

            else:
                print(soup.title.string)

                # curl -H "public-api-token: 52b1f183416b101f7096fbf897f2c674" -X PUT -d "urlToShorten=google.com" https://api.shorte.st/v1/data/url
                api_url = 'https://api.shorte.st/v1/data/url'

                data = {'urlToShorten': cleaned_data['url']}
                params = {'public-api-token': '52b1f183416b101f7096fbf897f2c674'}

                result = requests.put(api_url, headers=params, data=json.dumps(data))
                json_data = json.loads(result.text)
                result_data = json_data['shortenedUrl']
                print(result_data)
                error = False


                # Save the search result in databases
                curObject = ShortenURL(linkTitle = soup.title.string,
                                        urlToBeShortened = enteredURL,
                                        shortenedUrl = result_data
                                        )
                curObject.save()


        else:
            result_data = ''
            error = False
            enteredURL = ''

    else:
        error = False
        result_data = ''
        enteredURL = ''

    transaction = ShortenURLForm()

    context = {
        'error': error,
        'url_entered': enteredURL,
        'result': result_data,
        'url_form': transaction
    }

    return render(request, "shorturl/home.html", context)
