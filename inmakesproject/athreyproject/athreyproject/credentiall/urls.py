from . import views
from django.urls import path

urlpatterns = [

    path('register',views.register,name='register'),
    path('logins',views.logins,name='logins'),
    path('logout',views.logout,name='logout'),
]