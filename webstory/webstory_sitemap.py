from django.contrib.sitemaps import Sitemap
import os,json

class EntertainmentView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-entertainment.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/entertainment/"+item['url']+"/"
        return urls


class CovidView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-covid.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/covid/"+item['url']+"/"
        return urls

class CelebView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-celeb.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/celeb/"+item['url']+"/"
        return urls

class FoodView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-food.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/food/"+item['url']+"/"
        return urls



class FitnessView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-fitness.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/fitness/"+item['url']+"/"
        return urls

class FashionView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-fashion.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/fashion/"+item['url']+"/"
        return urls

class HealthView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-health.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/health/"+item['url']+"/"
        return urls

class BeautyView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-beauty.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/beauty/"+item['url']+"/"
        return urls




class SportsView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-sports.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/sports/"+item['url']+"/"
        return urls

class GamingView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-gaming.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/gaming/"+item['url']+"/"
        return urls

class TechView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-tech.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/tech/"+item['url']+"/"
        return urls

class LatestView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description-latest.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/latest/"+item['url']+"/"
        return urls

