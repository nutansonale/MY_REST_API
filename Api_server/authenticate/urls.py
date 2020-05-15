from django.urls import path
from authenticate import views


#authentication patterns
urlpatterns=[
    path('authreg/',views.auth_register),
    path('authlogin/',views.auth_login),
    path('getoken/',views.gettoken),
    path('allusers/',views.getallusers),
    path('logout/',views.deletuser)

]