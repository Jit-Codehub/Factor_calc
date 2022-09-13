"""polynomials_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from difference_between.sitemaps import *
from django.contrib.sitemaps.views import sitemap,index
from polynomials.views import aboutus,contactus,disclaimer,privacy_policy
from webstory.webstory_sitemap import *;
from django.views.static import serve
from django.conf import settings
from polynomials.Sitemaps import *;
sitemaps = {
    'Category-sitemap': Category_Sitemap,
   'Difference-Between-sitemap':Differ_Sitemap,
   'polynomials-addition-sitemap':poly_add_Sitemap,
     'polynomials-subtraction-sitemap':poly_sub_Sitemap,
     'polynomials-multiplication-sitemap':poly_mul_Sitemap,
     'polynomials-division-sitemap':poly_div_Sitemap,
     'is-expression-polynomial-sitemap':check_poly_Sitemap,
     'degree-of-polynomials-sitemap':degree_poly_Sitemap,
     'polynomial-in-ascending-order-sitemap':ascding_poly_Sitemap,
     'polynomial-in-descending-order-sitemap':descding_poly_Sitemap,
     'leading-polynomials-sitemap':leading_poly_Sitemap,
     'polynomials-factors-sitemap':fact_poly_Sitemap,
     'polynomials-gcf-sitemap':gcf_poly_Sitemap,
     'polynomials-gcf-factors-sitemap':gcf_fact_Sitemap,
     'polynomials-lcm-sitemap':poly_lcm_Sitemap,
     'prime-polynomials-sitemap':poly_prime_Sitemap,
     'polynomials-factor-as-adiition-difference-of-cube-sitemap':poly_fact_cube_Sitemap,
     'polynomials-factor-as-difference-of-square-sitemap':poly_fact_sqr_Sitemap,
     'binomial-expansion-sitemap':binom_expn_Sitemap,
     'polynomials-factor-over-complex-sitemap':fact_complex_Sitemap,
     'polynomials-root-sitemap':poly_root_Sitemap,
     'polynomial-remainder-theorm-sitemap':poly_remainder_Sitemap,
   'entertainment-sitemap':EntertainmentView,
   'covid-sitemap':CovidView,
   'celeb-sitemap':CelebView,
   'food-sitemap':FoodView,
   'fitness-sitemap':FitnessView,
   'fashion-sitemap':FashionView,
   'health-sitemap':HealthView,
   'beauty-sitemap':BeautyView,
   
   'sports-sitemap':SportsView,
   'gaming-sitemap':GamingView,
   'tech-sitemap':TechView,
   'latest-sitemap':LatestView,
   

}

urlpatterns = [
    path('about-us/',aboutus, name='about-us'),
    path('contact-us/',contactus, name='contact-us'),
    path('disclaimer/',disclaimer, name='disclaimer'),
    path('privacy-policy/',privacy_policy, name='privacy-policy'),
    path('admin/', admin.site.urls),
    path('', include('polynomials.urls')),
    path('web-stories/', include('webstory.urls')),
    path('difference-between/', include('difference_between.urls')),
    path('famous-people/', include('famous_people.urls')),
   
    path('sitemap.xml', index, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.index'),
    path('<section>.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

handler404 = 'webstory.views.handler404'