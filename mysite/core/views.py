from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mysite.core.models import LandOwner,CarOwner,Place,Security
from mysite.core.forms import LandOwnerSignUpForm
from mysite.core.forms import CarOwnerSignUpForm
from django.http import Http404
from django.http import HttpResponse


import requests
from pprint import pprint

# @login_required(login_url='/landowner/login/')
def home(request):
    return render(request, 'home.html')


def signup_landowner(request):
    if request.method == 'POST':
        form = LandOwnerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            # user.refresh_from_db()  # load the profile instance created by the signal
            email = form.cleaned_data.get('email')
            pincode = form.cleaned_data.get('pincode')
            lat = form.cleaned_data.get('lat')
            lon = form.cleaned_data.get('lon')
            slots = form.cleaned_data.get('slots')
            place = form.cleaned_data.get('place')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            l=LandOwner.objects.create(user=user,email=email,lat=lat,lon=lon,pincode=pincode,placename=place)
            Place.objects.create(placename=l,vacancy=slots)
            Security.objects.create(user=l)
            return redirect('landowner')
    else:
        form = LandOwnerSignUpForm()
    return render(request, 'signup_landowner.html', {'form': form})


def signup_carowner(request):
    if request.method == 'POST':
        form = CarOwnerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            user.save()
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            CarOwner.objects.create(user=user,email=email,name=name,phone=phone,)
            return redirect('carowner')
    else:
        form = CarOwnerSignUpForm()
    return render(request, 'signup_carowner.html', {'form': form})


@login_required(login_url='/carowner/login/')
def carowner(request):
    print(request.user)
    x=CarOwner.objects.all().get(user=request.user)
    return render(request,'carowner.html',{'carowner':x})

@login_required(login_url='/landowner/login/')
def landowner(request):
    print(request.user)
    x=LandOwner.objects.all().get(user=request.user)
    return render(request,'landowner.html',{'landowner':x})

@login_required(login_url='/carowner/login/')
def search(request):
    return render(request,'search.html')
            
@login_required(login_url='/carowner/login/')
def search_place(request,place_name):
    try:
        z = LandOwner.objects.all().get(placename=place_name)
        p = Place.objects.all().get(placename=z)
        p.vacancy=p.vacancy+1
        z.earnings=z.earnings+30
        z.save()
        p.save()
        print(z.user)
        print(p.placename.placename)
        return render(request,'search_place.html',{'landowner':z,'place':p})
    except:     
        return HttpResponse('<h1>This place does not exist</h1>')      

def find(l, coord):
  return min(l, key=lambda p:dist_sq(coord, p))

def dist_sq(a, b): # distance squared (don't need the square root)
        return (a[0] - b[0])**2 + (a[1] - b[1])**2

def takeClosest(myList, myNumber):
  closest = myList[0]
  for i in range(1, len(myList)):
    if abs(i - myNumber) < closest:
      closest = i
  return closest

@login_required(login_url='/carowner/login/')
def search_location(request,pin_code):           
    l = [(e.lat,e.lon) if e.lat is not None else (0,0) for e in LandOwner.objects.all() ]
    p = [e.pincode if Place.objects.all().get(placename=e).vacancy !=0 else 0 for e in LandOwner.objects.all()]
    print(l)
    print(p)
    responseip=requests.get('http://ipinfo.io/')
    responseip=responseip.json()
    city = responseip['city']
    responsedata = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e81aa24b21cefcb8f32a709177a63342")
    responsedata=responsedata.json()
    # print(responsedata)
    # print(responsedata['coord']['lat'])
    # print(responsedata['coord']['lon'])
    lon = responsedata['coord']['lon']
    lat = responsedata['coord']['lat']
    # l = [(35.9879845760485, -4.74093235801354), (35.9888687992442, -4.72708076713794), (35.9889733432982, -4.72758983150694), (35.9915751019521, -4.72772881198689), (35.9935223025608, -4.72814213543564), (35.9941433944962, -4.72867416528065), (35.9946670576458, -4.72915181755908), (35.995946587966, -4.73005565674077), (35.9961479762973, -4.7306870912609), (35.9963563641681, -4.7313535758683), (35.9968685892892, -4.73182757975504), (35.9976738530666, -4.73194429867996) ]
    coord = (lat,lon)
    closest=(takeClosest(p,int(pin_code)))
    print(p[closest])
    z = LandOwner.objects.all().get(pincode=p[closest])
    pp = Place.objects.all().get(placename=z)
    pp.vacancy=pp.vacancy-1
    z.earnings=z.earnings+30
    z.save()
    pp.save()
    print(pp)
    print(z)
    # print (find(l, coord))
    # x,y = find(l,coord)
    # nearest = LandOwner.objects.all().get(lat=x,lon=y)                    
    # print("City: "+str(city))
    # print("Weather conditions:"+str(responsedata['weather']['description']))
    # print("Temperature: "+str(responsedata['main']['temp']-273)+"C")
    # print("Humidity: "+str(responsedata['main']['humidity']))
    # vals ={'lat':lat,'lon':lon,'nearest':nearest}
    return render(request,'search_location.html',{'place':pp,'landowner':z})
                        
@login_required(login_url='/security/login/')
def security(request):
    x=LandOwner.objects.all().get(user=request.user)
    p=Place.objects.all().get(placename=x)
    print(p.vacancy)
    return render(request,'security.html',{'vacancy':p.vacancy})

@login_required(login_url='/security/login/')
def security_book(request):
    x=LandOwner.objects.all().get(user=request.user)
    p=Place.objects.all().get(placename=x)
    p.vacancy=p.vacancy-1
    p.save()
    return redirect('security')
                        
@login_required(login_url='/security/login/')
def security_vacate(request):
    x=LandOwner.objects.all().get(user=request.user)
    p=Place.objects.all().get(placename=x)
    p.vacancy=p.vacancy+1
    p.save()
    return redirect('security')
                        



