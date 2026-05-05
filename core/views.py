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
    try:
        data=requests.get(url,params=param).json()
        if 'city' not in data:
            messages.error(request,'City not Found!!!')
            return render(request, "index.html")
     
        temp=data['main']["temp"]
        desc=data["weather"][0]["description"]
        visibility=data["visibility"]
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        windspeed=data['wind']['speed']
        icon = data["weather"][0]["icon"]
        return render(request,'index.html',{'temp':temp,'city':city,'desc':desc,'visibility':visibility,'humidity':humidity,'pressure':pressure,'windspeed':windspeed,'icon':icon})
    except Exception as e:
       messages.error(request,"Could not fetch the data!!")
       return render(request, "index.html")



