"""
URL configuration for todolist_project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name="register"),
    path('', include("main.urls")),
    path('', include("django.contrib.auth.urls"))
]

# You must create a link to URLs for every different applications you created.
# The specified path is crucial as it goes to the related views once the path is matched in the root level.

# When 'django.contrib.auth.urls' included, the project will support these following URL patterns:
#   <path>/login/ [name='login']   (registration/login.html)
#   <path>/logout/ [name='logout']   (registration/logged_out.html)
#   <path>/password_change/ [name='password_change']   (registration/password_change_form.html)
#   <path>/password_change/done/ [name='password_change_done']   (registration/password_change_done.html)
#   <path>/password_reset/ [name='password_reset']   (registration/password_reset_email.html)
#   <path>/password_reset/done/ [name='password_reset_done']   (registration/password_reset_done.html)
#   <path>/reset/<uidb64>/<token>/ [name='password_reset_confirm']   (registration/password_reset_confirm.html)
#   <path>/reset/done/ [name='password_reset_complete']   (registration/password_reset_complete.html)
# With this inclusion, it will now look in the URLs file there, and see if we have a valid URL.