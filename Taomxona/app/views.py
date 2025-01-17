from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Food
from django.contrib.auth.forms import UserCreationForm
from .forms import MessageForm
from django.contrib.auth.decorators import permission_required, login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect



def home(request):
    foods = Food.objects.all()
    return render(request, 'home.html', {'foods': foods})

class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'
    context_object_name = 'foods'

class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'
    context_object_name = 'food'

class FoodCreateView(CreateView):
    model = Food
    template_name = 'food_form.html'
    fields = ['category', 'name', 'description', 'price', 'image']
    success_url = reverse_lazy('food_list')

class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'food_form.html'
    fields = ['category', 'name', 'description', 'price', 'image']
    success_url = reverse_lazy('food_list')

class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food_confirm_delete.html'
    success_url = reverse_lazy('food_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['lochinbekrasuljonovdev@gmail.com'],
            )
            return render(request, 'message_sent.html')
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})


def search_foods(request):
    query = request.GET.get('q')
    foods = Food.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)) if query else []
    return render(request, 'search_results.html', {'foods': foods, 'query': query})

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})