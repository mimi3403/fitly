from django.shortcuts import render, redirect
from .models import Elog, UserProfile
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ProfileForm, ElogForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  return render(request, 'user/signup.html')

def profile_form(request, user_id):
  form = ProfileForm(request.POST)
  if form.is_valid():
    new_form = form.save(commit=False)
    new_form.user_id = user_id
    new_form.save()
  return redirect('profile', user_id=user_id)

def profile(request, user_id):
  user = UserProfile.objects.get(id=user_id)
  profile_form = ProfileForm()
  return render(request, 'user/profile.html', {
    'user': user,
    'profile_form': profile_form
  })

class ElogCreate(CreateView):
  model = Elog
  fields = [ 
    'date_time',
    'name', 
    'distance_miles', 
    'length_of_time', 
    'reps_laps', 
    'weight_pounds', 
    'intensity', 
    'pace_minutes_per_mile', 
    'calories_burned']

def get_initial(self):
    return { 'user_id': self.request.user }

class ElogUpdate(UpdateView):
  model = Elog
  fields = [ 
    'name', 
    'distance_miles', 
    'length_of_time', 
    'reps_laps', 
    'weight_pounds', 
    'intensity', 
    'pace_minutes_per_mile', 
    'calories_burned']

class ElogDelete(DeleteView):
  model = Elog
  success_url = '/elogs/'

def elogs_index(request):
  elogs = Elog.objects.all()
  return render(request, 'elogs/index.html', {'elogs': elogs})

def elogs_detail(request, user_id):
  userprofile = UserProfile.objects.get(id=user_id)
  return render(request, 'elogs/detail.html', {'userprofile': userprofile})
