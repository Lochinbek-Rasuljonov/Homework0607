from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('foods/', views.FoodListView.as_view(), name='all_foods'),
    path('food/<int:food_id>/', views.FoodDetailView.as_view(), name='food_detail'),
    path('food/add/', views.FoodCreateView.as_view(), name='add_food'),
    path('food/edit/<int:food_id>/', views.FoodUpdateView.as_view(), name='edit_food'),
    path('food/delete/<int:food_id>/', views.FoodDeleteView.as_view(), name='delete_food'),
    path('send_message/', views.send_message, name='send_message'),
    path('search/', views.search_foods, name='search_foods'),
    path('profile/', views.profile_view, name='profile'),
]