
SIGNUP LandOWNER
def signup_landowner(request):
    if request.method == 'POST':
        form = LandOwnerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            # user.refresh_from_db()  # load the profile instance created by the signal
            email = form.cleaned_data.get('email')
            lat = form.cleaned_data.get('lat')
            lon = form.cleaned_data.get('lon')
            place = form.cleaned_data.get('place')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            l=LandOwner.objects.create(user=user,email=email,lat=lat,lon=lon,placename=place)
            Place.objects.create(placename=l)
            return redirect('home')
    else:
        form = LandOwnerSignUpForm()
    return render(request, 'signup_landowner.html', {'form': form})

