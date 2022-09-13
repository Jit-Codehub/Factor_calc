from django.urls import path
from .views import *
urlpatterns = [
    path('',differ_func, name='differ_func'),
    path('<str:slug>/', difference_btn,name='difference_btn'),

]