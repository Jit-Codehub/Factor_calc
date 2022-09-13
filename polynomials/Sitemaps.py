from django.contrib.sitemaps import Sitemap
from .urls import urlpatterns
from django.shortcuts import reverse
from datetime import datetime
from django.contrib import admin
from django.urls import path, include 
from .models import *

class poly_add_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return add_poly_db.objects.all()

    def location(self, obj):
        return obj.slug

    def lastmod(self, obj): 
        return obj.date_modified
class poly_sub_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return sub_poly_db.objects.all()

    def location(self, obj):
        return obj.slug

    def lastmod(self, obj): 
        return obj.date_modified
class poly_mul_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return mul_poly_db.objects.all()

    def location(self, obj):
        return obj.slug

    def lastmod(self, obj): 
        return obj.date_modified
class poly_div_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return div_poly_db.objects.all()

    def location(self, obj):
        return obj.slug

    def lastmod(self, obj): 
        return obj.date_modified

class check_poly_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return check_poly_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class degree_poly_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return degree_poly_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class ascding_poly_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return ascding_poly_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class descding_poly_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return descding_poly_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class leading_poly_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return leading_poly_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class fact_poly_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return fact_poly_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class gcf_poly_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return gcf_poly_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class gcf_fact_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return gcf_fact_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified

class poly_lcm_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return poly_lcm_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class poly_prime_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return poly_prime_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class poly_fact_cube_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return poly_fact_cube_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class poly_fact_sqr_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return poly_fact_sqr_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class binom_expn_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return binom_expn_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class fact_complex_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return fact_complex_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class poly_root_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return poly_root_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
class poly_remainder_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return poly_remainer_db.objects.all()

    def location(self, obj):
        print(obj.slug)
        return obj.slug
    def lastmod(self, obj): 
        return obj.date_modified
polynomials={
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
}