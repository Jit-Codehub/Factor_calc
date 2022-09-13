from django.urls import path,include
from .views import *

urlpatterns = [
    path('',homepage, name='home'),
    path('humor/',humor,name='humor'),
    path('celeb/',celeb,name='celeb'),
    path('beauty/',beauty,name='beauty'),
    path('latest/',latest,name='latest'),
    path('covid/',covid,name='covid'),
    path('food/',food,name='food'),
    path('gaming/',gaming,name="gaming"),
    path('entertainment/',entertainment,name='entertainment'),

    path('travel/',travel,name='travel'),
    path('tech/',tech,name='tech'),
    path('wellness/',wellness,name='wellness'),
    path('fashion/',fashion,name='fashion'),
    path('health/',health,name='health'),
    path('sports/',sports,name='sports'),
    path('fitness/',fitness,name='fitness'),

    path('<str:category>/<str:story>/',webstories,name='webstories')
]
import webstory.jobs  # NOQA @isort:skip
import logging
logging.basicConfig(level="DEBUG")