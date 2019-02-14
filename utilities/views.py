import os
import requests
from django.shortcuts import render
from datetime import datetime, timedelta




# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
    
def bye(request):
    datetimenow = datetime.now()
    bye_time = datetime(2019, 2, 28)
    bye_d_day = bye_time - datetimenow
    return render(request, 'utilities/bye.html', {'bye_time':bye_time, 'bye_d_day':bye_d_day})
    
def graduation(request):
    datetimenow = datetime.now()
    graduation_day = datetime(2019, 5, 28)
    graduation_d_day = graduation_day - datetimenow
    return render(request, 'utilities/graduation.html', {'graduation_day':graduation_day, 'graduation_d_day':graduation_d_day})

def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    # key = '7b22036c135688ac66ab6099cb947e73'
    datetimenow = datetime.now()
    token = os.getenv("key")
    url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID="+token
    req = requests.get(url).json()
    weather = req['weather'][0]['main']
    temp = int(req['main']['temp'])-273
    return render(request, 'utilities/today.html', {'weather':weather, 'temp':temp, 'datetimenow':datetimenow})
    
def ascii_new(request):
    fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    return render(request, 'utilities/ascii_new.html', {'fonts':fonts})
    
def ascii_make(request):
    text_1 = request.GET.get('text_1')
    font = request.GET.get('font')
    url = f"http://artii.herokuapp.com/make?text={text_1}&font={font}"
    req = requests.get(url).text

    return render(request, 'utilities/ascii_make.html', {'req':req})
    
def original(request):
    return render(request, 'original.html')
    
def translated(request):
    return render(request, 'translated.html')