from django.conf import settings
import os 

os.makedirs(os.path.join(settings.MEDIA_ROOT, "famous_people/images"), exist_ok=True)
os.makedirs(os.path.join(settings.MEDIA_ROOT, "temp"), exist_ok=True)