from. import views
from django.urls import path
from athreyproject import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.demo,name='demo'),
   # path('add/',views.addition,name='addition'),
    #path('sub/',views.subtraction,name='subtraction'),
    #path('mul/',views.mulitiplication,name='mulitiplication'),
    #path('div/', views.division,name='division')
     ]