from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('register/',register,name='register'),
    path('logout/',logout_page,name='logout'),
    path('login/',login_page,name='login'),
    path('works/',work_page,name='work'),
    path('educate/',educate_page,name='educate'),
    path('award/',award_page,name='award'),
    path('experience/',experience_page,name='experience'),
]
