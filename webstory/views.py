from re import I
from django.shortcuts import render
import json

def covid(request):
    
    file=open('media/web-stories/title-description-covid.json')
    data=json.load(file)
    context={}    
    context['titles']=data
   
    context['category']='covid'
    return render(request,'web_stories/home.html',context)

def celeb(request):
    
    file=open('media/web-stories/title-description-celeb.json')
    data=json.load(file)
    context={}    
    context['titles']=data
   
    context['category']='celeb'
    return render(request,'web_stories/home.html',context)

def food(request):
    
    file=open('media/web-stories/title-description-food.json')
    data=json.load(file)
    context={}    
    context['titles']=data
   
    context['category']='food'
    return render(request,'web_stories/home.html',context)

def humor(request):
    file=open('media/web-stories/title-description-humor.json')
    data=json.load(file)
    context={}    
    context['titles']=data
   
    context['category']='humor'
    return render(request,'web_stories/home.html',context)
def lifestyle(request):
    file=open('media/web-stories/title-description-lifestyle.json')
    data=json.load(file)
    context={}
       
    context['titles']=data
   
    context['category']='lifestyle'
    return render(request,'web_stories/home.html',context)
def fitness(request):
    file=open('media/web-stories/title-description-fitness.json')
    data=json.load(file)
    context={}
    
    context['titles']=data
  
    context['category']='fitness'
    return render(request,'web_stories/home.html',context)
def fashion(request):
    file=open('media/web-stories/title-description-fashion.json')
    data=json.load(file)
    context={}
 
    context['titles']=data
   
    context['category']='fashion'
    return render(request,'web_stories/home.html',context)

def health(request):
    file=open('media/web-stories/title-description-health.json')
    data=json.load(file)
    context={}

    context['titles']=data
    
    context['category']='health'
    return render(request,'web_stories/home.html',context)

def beauty(request):
    file=open('media/web-stories/title-description-beauty.json')
    data=json.load(file)
    context={}
    context['titles']=data
    context['category']='beauty'
    return render(request,'web_stories/home.html',context)
def entertainment(request):
    file=open('media/web-stories/title-description-entertainment.json')
    data=json.load(file)
    context={}
    context['titles']=data
    context['category']='entertainment'
    return render(request,'web_stories/home.html',context)

def latest(request):
    file=open('media/web-stories/title-description-latest.json')
    data=json.load(file)
    context={}
    context['titles']=data
    context['category']='latest'
    return render(request,'web_stories/home.html',context)

def tech(request):
    file=open('media/web-stories/title-description-tech.json')
    data=json.load(file)
    context={}
    context['titles']=data
    context['category']='tech'
    return render(request,'web_stories/home.html',context)

def gaming(request):
    file=open('media/web-stories/title-description-gaming.json')
    data=json.load(file)
    context={}
    context['titles']=data
    context['category']='gaming'
    return render(request,'web_stories/home.html',context)

def sports(request):
    file=open('media/web-stories/title-description-sports.json')
    data=json.load(file)
    context={}
    context['titles']=data
    context['category']='sports'
    return render(request,'web_stories/home.html',context)

def travel(request):
    file=open('media/web-stories/title-description-travel.json')
    data=json.load(file)
    context={}
    context['titles']=data
    context['category']='travel'
    return render(request,'web_stories/home.html',context)

def wellness(request):
    file=open('media/web-stories/title-description-wellness.json')
    data=json.load(file)
    context={}
    context['titles']=data
    context['category']='wellness'
    return render(request,'web_stories/home.html',context)

def homepage(request):
    return render(request,'web_stories/home_base.html')

#web stories
def webstories(request,story,category):
    context={}
    webno=story
    file=open('media/web-stories/webstory-'+str(webno)+"/webstory-"+str(webno)+".json")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%",file)
    data=json.load(file)
    context['data']=data
    context['webno']=webno
    if category == 'beauty':
        file=open('media/web-stories/title-description-beauty.json')
    elif category == 'latest':
        file=open('media/web-stories/title-description-latest.json')
    elif category == 'fashion':
        file=open('media/web-stories/title-description-fashion.json')
    elif category == 'health':
        file=open('media/web-stories/title-description-health.json')
    elif category == 'lifestyle':
        file=open('media/web-stories/title-description-lifestyle.json')
    elif category=='entertainment':
        file=open('media/web-stories/title-description-entertainment.json')
    elif category=='covid':
        file=open('media/web-stories/title-description-covid.json')
    elif category == 'fitness':
        file=open('media/web-stories/title-description-fitness.json')
    elif category == 'food':
        file=open('media/web-stories/title-description-food.json')
    elif category == 'gaming':
        file=open('media/web-stories/title-description-gaming.json')
    elif category == 'humor':
        file=open('media/web-stories/title-description-humor.json')
    elif category=='sports':
        file=open('media/web-stories/title-description-sports.json')
    elif category=='celeb':
        file=open('media/web-stories/title-description-celeb.json')
    elif category=='travel':
        file=open('media/web-stories/title-description-travel.json')
    elif category=='tech':
        file=open('media/web-stories/title-description-tech.json')
    else:
        file=open('media/web-stories/title-description-wellness.json')
    data=json.load(file)
    for i in data:
        if i['url']==webno:
            context['titles']=i
            return render(request,'web_stories/webstory.html',context)
    
def handler404(request, exception):
       
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')


