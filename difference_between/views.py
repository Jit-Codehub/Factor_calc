from django.shortcuts import render
from .models import category,Differ
from django.core.paginator import Paginator

# Create your views here.
def difference_btn(request,slug):
    try:
        try:
            try:
                catry=category.objects.get(sub_name=slug.replace('-',' ').title())
    
            except:
                catry=category.objects.get(sub_name=slug.replace('-',' ').upper())
            print(catry.id)
            sub_urls=Differ.objects.filter(subject_id=catry.id)
            print(sub_urls)
            if len(sub_urls)>0:
                categories=category.objects.all()
                paginator = Paginator(sub_urls, 10)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request,'difference_between/category.html',{'page_obj':page_obj,'title':slug.replace('-',' ').title(),'sub_urls':sub_urls,'categories':categories})
        except:
            pass
        body=Differ.objects.filter(slug=slug)[0]
        id=body.id
        print(id)
        categories=category.objects.all()
        next_three = Differ.objects.filter(id__gt=id)[:7]
        previous_three = Differ.objects.filter(id__lt=id).order_by('-id')[:8]
        return render(request,'difference_between/miscellaneous_data.html',{'body':body.content,'title':body.header,'header':body.header,'previous_three':previous_three,'next_three':next_three,'categories':categories})
    except:
        return render(request,'404.html')
def differ_func(request):
    subject=category.objects.all()
    subject1=subject[:len(subject)//2+1]
    subject2=subject[len(subject)//2+1:]
    print(subject)
    return render(request,'difference_between/subject.html',{'subject1':subject1,'subject2':subject2})
