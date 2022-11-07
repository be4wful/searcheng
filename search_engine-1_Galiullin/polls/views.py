from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render,redirect
from polls import main
import requests, bs4

def search_sentence(request):
    req = requests.get(
        'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B5%D0%BB%D0%B0%D0%B1%D1%83%D0%B3%D0%B0')
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    p3 = soup.select('.temperature .p3')
    weather1 = p3[0].getText()
    p4 = soup.select('.temperature .p4')
    weather2 = p4[0].getText()
    p5 = soup.select('.temperature .p5')
    weather3 = p5[0].getText()
    p6 = soup.select('.temperature .p6')
    weather4 = p6[0].getText()
    morning = 'Утром :' + weather1 + ' ' + weather2
    day = 'Днём :' + weather3 + ' ' + weather4
    p = soup.select('.rSide .description')
    weather = p[0].getText()
    w = weather.strip()
    if 'q' in request.GET and request.GET["q"] != '':
        result = main.search_sentence(request.GET["q"])
        if result != '':
            return render(request, 'polls/index.html', context={"sentences": result, 'w': w, 'morning': morning, 'day': day})
        elif (request.GET["q"]) == ' ':
            return render(request, 'polls/index.html', context={"new": '', 'w': w, 'morning': morning, 'day': day})
        return render(request, 'polls/index.html', context={"sentences": '0 результатов поиска', 'w': w, 'morning': morning, 'day': day})
    else:
        return render(request, 'polls/index.html', {'w': w, 'morning': morning, 'day': day})
