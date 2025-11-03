from django.urls import path
from . import views

# This urls.py represents the URLs that go to the different views, available in views.py.

urlpatterns = [
    path('view-list-items/<int:id>', views.view_add_list_items, name="view list items"),
    # path('<str:name>', views.index, name="index"),
    path('view-list/', views.view_list, name="view user lists"),
    path('create-list/', views.create_list, name="create new user list"),
    path('about/', views.about, name="about"),
    path('profile/', views.user_profile, name="user profile"),
    path('simple-view/', views.simple_view, name="simple view"),
    path('', views.home, name="home page")
]