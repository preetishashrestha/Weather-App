from django.shortcuts import render
import requests
from django.contrib import messages
# Create your views here.
def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='Kathmandu'
    
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf22686cf11682e29d657b984d138978'
    param={"units":"metric"}
    city_url=f"https://api.unsplash.com/search/photos?query={city}&per_page=1&client_id=h8_DOz2TT0Ha8YmR4HD-6IwbE0-jww76mVUigFKlnSs"
    response=requests.get(city_url).json()
    city_image=response["results"][0]["urls"]["regular"]
    try:
        data=requests.get(url,params=param).json()
        temp=data['main']["temp"]
        desc=data["weather"][0]["description"]
        visibility=data["visibility"]
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        windspeed=data['wind']['speed']
        icon = data["weather"][0]["icon"]
        return render(request,'index.html',{'temp':temp,'city':city,'desc':desc,'visibility':visibility,'humidity':humidity,'pressure':pressure,'windspeed':windspeed,'icon':icon,'city_image':city_image})
        
     
        
    except Exception as e:
       temp =0
       desc='no city'
       messages.error(request,"Could not fetch the data!!")
       return render(request,'index.html',{'temp':temp,'city':city,'desc':desc})


'''

'''