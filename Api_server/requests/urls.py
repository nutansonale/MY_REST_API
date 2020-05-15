from django.urls import path
from requests import views


#requests patterns
urlpatterns=[
    path('request/',views.requestQ),

]