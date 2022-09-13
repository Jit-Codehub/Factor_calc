from django.urls import path
from .views import *

app_name = "famous_people"

urlpatterns = [
    path('', HomePageView.as_view(), name="home_url"),
    path('portal/', PortalUploadData.as_view(), name="portal_upload_data_url"),
    path('<slug:title_slug>-facts/',PostPageView.as_view(),name='post_url'),
]