import json
from django.http import Http404
from django.views.generic import TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import saveDataInDB
from .models import *
from django.conf import settings
import os


class PortalUploadData(LoginRequiredMixin, TemplateView):
    login_url = "/admin/login/"
    template_name = "famous_people/portal_upload_data.html"
    extra_context = {}

    def get(self, request, *args, **kwargs):
        self.extra_context["msg"] = ""
        self.extra_context["famous_random_peoples_header"] = FamousPeople.objects.all().order_by("?")[:5]
        self.extra_context["famous_random_peoples_footer"] = FamousPeople.objects.all().order_by("?")[:15]
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        json_file = request.FILES.get("json_file")
        try:
            if not json_file:
                json_file = open(os.path.join(settings.MEDIA_ROOT,"temp","famous_people.json"),encoding="utf-8")
            data = json.load(json_file)
            res = saveDataInDB(data,json_file.name)
            msg = f"<span style='color:green;'>Success : {res}</span>"
        except Exception as e:
            msg = f"<span style='color:red;'>Error : {e}</span>"
        self.extra_context["msg"] = msg
        return super().get(request, *args, **kwargs)


class HomePageView(ListView):
    template_name = "famous_people/homepage.html"
    extra_context = {}
    paginate_by = 100

    def get_queryset(self):
        return FamousPeople.objects.all().order_by("-id")

    def get(self, *args, **kwargs):
        self.extra_context["famous_random_peoples_header"] = FamousPeople.objects.all().order_by("?")[:5]
        self.extra_context["famous_random_peoples_footer"] = FamousPeople.objects.all().order_by("?")[:15]
        return super().get(*args, **kwargs)
    

class PostPageView(TemplateView):
    template_name = "famous_people/post_page.html"
    extra_context = {}

    def get(self, *args, **kwargs):
        title_slug = self.kwargs.get("title_slug")
        famous_people_obj = FamousPeople.objects.filter(slug=title_slug)
        if famous_people_obj:
            famous_people_obj = famous_people_obj.first()
            self.extra_context["famous_people_obj"] = famous_people_obj
            self.extra_context["jump_links"] = json.loads(famous_people_obj.jump_links)
            self.extra_context["birthday_highlights"] = json.loads(famous_people_obj.birthday_highlights)
            self.extra_context["facts"] = json.loads(famous_people_obj.facts)
            self.extra_context["famous_random_peoples_header"] = FamousPeople.objects.all().order_by("?")[:5]
            self.extra_context["famous_random_peoples_footer"] = FamousPeople.objects.all().order_by("?")[:15]
            return super().get(*args, **kwargs)
        else:
            raise Http404