from django.shortcuts import render,redirect
import datetime
from .utilities import *
from .models import *
def home(request):
         return render(request,'base/home.html')
def aboutus(request):
         return render(request,'base/about_us.html')
def contactus(request):
         return render(request,'base/contact_us.html')
def disclaimer(request):
         return render(request,'base/disclaimer.html')
def privacy_policy(request):
         return render(request,'base/privacy_policy.html')
def polynomials_calculator(request):
 return render(request,'base/polynomials-calculator.html')
def poly_add(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/adding-polynomials-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/add_poly.html')
def poly_add_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/adding-polynomials-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if add_poly_db.objects.filter(inputEnter=num1).exists():
                db=add_poly_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:

                s=poly_addition_func(num1)
                b=add_poly_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/adding-polynomials-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Adding Polynomials {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/add_poly_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except:
        return redirect('/adding-polynomials-calculator/')
def poly_sub(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/subtracting-polynomials-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/sub_poly.html')
def poly_sub_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/subtracting-polynomials-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if sub_poly_db.objects.filter(inputEnter=num1).exists():
                db=sub_poly_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:

                s=poly_substraction_func(num1)
                b=sub_poly_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/subtracting-polynomials-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Subtracting Polynomials {}'.format(num1),date_modified=date.today())
                b.save()
            
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/sub_poly_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)   
        return redirect('/subtracting-polynomials-calculator/')
def poly_mul(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/multiplying-polynomials-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/mul_poly.html')
def poly_mul_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/multiplying-polynomials-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if mul_poly_db.objects.filter(inputEnter=num1).exists():
                db=mul_poly_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=poly_multiplication_func1(num1)
                b=mul_poly_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/multiplying-polynomials-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Multiplying Polynomials {}'.format(num1),date_modified=date.today())
                b.save()
            
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/mul_poly_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except:
        return redirect('/multiplying-polynomials-calculator/')

def poly_div(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/dividing-polynomials-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/div_poly.html')
def poly_div_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/dividing-polynomials-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if div_poly_db.objects.filter(inputEnter=num1).exists():
                db=div_poly_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=poly_division_func(num1)
                b=div_poly_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/dividing-polynomials-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Dividing Polynomials {}'.format(num1),date_modified=date.today())
                b.save()
            try:    
                s[1]=eval(s[1])
            except:
                pass
            num1=num1.replace('-by-','/')
            print(s[1][0])
            print(s[1][1])
            print(s[1])
            return render(request, 'Polynomials/div_poly_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1][0],'result1':s[1][1]})
    except:
        return redirect('/dividing-polynomials-calculator/')
def poly_check(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/is-{}-a-polynomial/'.format(res1))
    else:
        return render(request, 'Polynomials/check_poly.html')
def poly_check_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/is-{}-a-polynomial/'.format(res1))
            else:
                eval('s_p')
        except:
            if check_poly_db.objects.filter(inputEnter=num1).exists():
                db=check_poly_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=compare_expr_func(num1)
                b=check_poly_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/is-{}-a-polynomial/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Is {} a Polynomial'.format(num1),date_modified=date.today())
                b.save()
            print(s[1])
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/check_poly_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/determining-if-the-expression-is-a-polynomial-calculator/')
def poly_degree(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/degree-of-a-polynomial-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/degree_poly.html')
def poly_degree_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/degree-of-a-polynomial-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if degree_poly_db.objects.filter(inputEnter=num1).exists():
                db=degree_poly_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=degree_pol_func(num1)
                b=degree_poly_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/degree-of-a-polynomial-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Degree of Polynomial {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/degree_poly_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except:
        return redirect('/degree-of-a-polynomial-calculator/')

def poly_ascend(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/polynomial-in-ascending-order-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/poly_ascend.html')
def poly_ascend_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/polynomial-in-ascending-order-{}/'.format(res1))
            else:
                return redirect('/polynomial-in-ascending-order-calculator/')
        except:
            if ascding_poly_db.objects.filter(inputEnter=num1).exists():
                db=ascding_poly_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=poly_ascending_func(num1)
                b=ascding_poly_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/polynomial-in-ascending-order-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='ascending of Polynomial {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/poly_ascend_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/polynomial-in-ascending-order-calculator/')

def poly_descnd(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/polynomial-in-descending-order-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/poly_descend.html')
def poly_descnd_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/polynomial-in-descending-order-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if descding_poly_db.objects.filter(inputEnter=num1).exists():
                db=descding_poly_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=poly_descending_func(num1)
                b=descding_poly_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/polynomial-in-descending-order-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='descending of Polynomial {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/poly_descend_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except:
        return redirect('/polynomial-in-descending-order-calculator/')

def leading_poly(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/leading-term-of-a-polynomial-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/poly_lead.html')
def leading_poly_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/leading-term-of-a-polynomial-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if leading_poly_db.objects.filter(inputEnter=num1).exists():
                db=leading_poly_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=eval(db[0].finalAnswer)
            else:
                s=leading_func(num1)
                b=leading_poly_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/leading-term-of-a-polynomial-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='lead term of Polynomial {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/poly_lead_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1][0],'result1':s[1][1]})
    except Exception as e:
        print(e)
        return redirect('/leading-term-of-a-polynomial-calculator/')

def factor_poly(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/factoring-multi-variable-polynomials-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/poly_fact_mul.html')
def factor_poly_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/factoring-multi-variable-polynomials-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if fact_poly_db.objects.filter(inputEnter=num1).exists():
                db=fact_poly_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=factor_multiple_func(num1)
                b=fact_poly_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/factoring-multi-variable-polynomials-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='factor over multi variable Polynomial {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/poly_fact_mul_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/factoring-multi-variable-polynomials-calculator/')

def gcf_poly(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/gcf-of-polynomials-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/poly_gcf.html')
def gcf_poly_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/gcf-of-polynomials-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if gcf_poly_db.objects.filter(inputEnter=num1).exists():
                db=gcf_poly_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=poly_gcf_func(num1)
                b=gcf_poly_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/gcf-of-polynomials-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Poly GCF of Polynomial {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/poly_gcf_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/gcf-of-polynomials-calculator/')

def gcf_fact(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/factor-out-gcf-from-polynomials-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/gcf_fact.html')
def gcf_fact_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/factor-out-gcf-from-polynomials-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if gcf_fact_db.objects.filter(inputEnter=num1).exists():
                db=gcf_fact_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=poly_gcf_func1(num1)
                b=gcf_fact_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/factor-out-gcf-from-polynomials-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Factor Out GCF Polynomial {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/gcf_fact_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/factor-out-gcf-from-polynomials-calculator/')


def poly_lcm(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        res2=request.POST['textfield2']
        res2=res2.replace('^','~')
        res2=res2.replace('+','_')
        res2=res2.replace('/','-div-')
        res2=res2.replace(' ','')
        return  redirect('/lcm-of-polynomials-{}-and-{}-using-gcf/'.format(res1,res2))
    else:
        return render(request, 'Polynomials/poly_lcm.html')
def poly_lcm_func(request,num1,num2):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        num2=num2.replace('~','^')
        num2=num2.replace('_','+')
        num2=num2.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']) or (num2) != (request.POST['textfield2']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                res2=request.POST['textfield2']
                res2=res2.replace('^','~')
                res2=res2.replace('+','_')
                res2=res2.replace('/','-div-')
                res2=res2.replace(' ','')
                return  redirect('/lcm-of-polynomials-{}-and-{}-using-gcf/'.format(res1,res2))
            else:
                eval('s_p')
        except:
            if poly_lcm_db.objects.filter(inputEnter=num1+' X '+num2).exists():
                db=poly_lcm_db.objects.filter(inputEnter=num1+' X '+num2)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=poly_lcm_using_gcf_func(num1+','+num2)
                b=poly_lcm_db(inputEnter=num1+' X '+num2,detailStep=s[0],finalAnswer=s[1],slug='/lcm-of-polynomials-{}-and-{}-using-gcf/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-'),num2.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='LCM of {},{}'.format(num1,num2),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            num2=num2.replace('-by-','/')
            return render(request, 'Polynomials/poly_lcm_detail.html',{'input1':num2,'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/lcm-of-polynomials-using-gcf-calculator/')

def poly_prime(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/determining-if-{}-polynomial-is-prime/'.format(res1))
    else:
        return render(request, 'Polynomials/poly_prime.html')
def poly_prime_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/determining-if-{}-polynomial-is-prime/'.format(res1))
            else:
                eval('s_p')
        except:
            if poly_prime_db.objects.filter(inputEnter=num1).exists():
                db=poly_prime_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=poly_prime_soln_func(num1)
                b=poly_prime_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/determining-if-{}-polynomial-is-prime/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Prime Polynomial {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            z=s[1].replace('It is not a Prime Polynomial due to it has more than 2 factors','It has factors').replace('It is a prime polynomial because it has only two factors i.e','It has factors')
            return render(request, 'Polynomials/poly_prime_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1],'result1':z})
    except Exception as e:
        print(e)
        return redirect('/determining-if-polynomial-is-prime-calculator/')

def poly_factor_cube(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/factoring-binomials-as-sum-or-difference-of-cubes-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/poly_sum_diff_cube_home.html')
def poly_factor_cube_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/factoring-binomials-as-sum-or-difference-of-cubes-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if poly_fact_cube_db.objects.filter(inputEnter=num1).exists():
                db=poly_fact_cube_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=sum_sub_cube(num1)
                b=poly_fact_cube_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/factoring-binomials-as-sum-or-difference-of-cubes-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Factor Binomial as sum or diff of cube {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/poly_sum_diff_cube.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/factoring-binomials-as-sum-or-difference-of-cubes-calculator/')

def poly_factor_sqr(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/factoring-difference-square-polynomial-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/poly_sum_diff_sqr.html')
def poly_factor_sqr_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/factoring-difference-square-polynomial-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if poly_fact_sqr_db.objects.filter(inputEnter=num1).exists():
                db=poly_fact_sqr_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=factor_diff_sqr_func(num1)
                b=poly_fact_sqr_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/factoring-difference-square-polynomial-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Factor Binomial as diff of square {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/poly_sum_diff_sqr_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/factoring-difference-square-polynomial-calculator/')


def poly_expn(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/binomial-expansion-of-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/binomial_expand.html')
def poly_expn_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if num1 != request.POST['textfield1']:
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/binomial-expansion-of-{}/'.format(res1))
            else:
                eval('s_d')
        except:
            if binom_expn_db.objects.filter(inputEnter=num1).exists():
                db=binom_expn_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=poly_expand_binomial_theorm_func(num1)             
                b=binom_expn_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/binomial-expansion-of-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Binomial Expansion {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/binomial_expand_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/binomial-expansion-calculator/')

def comp_fact(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/factoring-{}-over-complex-numbers/'.format(res1))
    else:
        return render(request, 'Polynomials/fact_over_complex.html')
def comp_fact_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/factoring-{}-over-complex-numbers/'.format(res1))
            else:
                eval('s_p')
        except:
            if fact_complex_db.objects.filter(inputEnter=num1).exists():
                db=fact_complex_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
                print(s[0])
            else:
                s=list(poly_factor_over_complex1_func(num1))
                #print(s[0])
                
                b=fact_complex_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/factoring-{}-over-complex-numbers/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Factor Over Complex {}'.format(num1),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')

            s[0]=s[0].replace('<p>=</p>','')
            return render(request, 'Polynomials/fact_over_complex_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/factoring-over-complex-numbers-calculator/')

def polynomial_root(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        return  redirect('/polynomial-root-of-{}/'.format(res1))
    else:
        return render(request, 'Polynomials/poly_root.html')
def polynomial_root_func(request,num1):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                return  redirect('/polynomial-root-of-{}/'.format(res1))
            else:
                eval('s_p')
        except:
            if poly_root_db.objects.filter(inputEnter=num1).exists():
                db=poly_root_db.objects.filter(inputEnter=num1)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=list(poly_root_func(num1))
                
                b=poly_root_db(inputEnter=num1,detailStep=s[0],finalAnswer=s[1],slug='/polynomial-root-of-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='Factor Over Complex {}'.format(num1),date_modified=date.today())
                b.save()
            s[0]=s[0].replace('\\sqrt','√').replace('sqrt','√')
            s[1]=s[1].replace('\\sqrt','√').replace('sqrt','√')
            num1=num1.replace('-by-','/')
            return render(request, 'Polynomials/poly_root_detail.html',{'input1':num1.replace('÷',' and '),'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/polynomial-root-calculator/')



#POLY EQUATION SOLVER VIEW
def poly_eq_solver(request):
    return render(request, "Polynomials/poly_eq_solver.html")
def remainder_theorem_calculator(request):
    if request.method == 'POST':
        res1=request.POST['textfield1']
        res1=res1.replace('^','~')
        res1=res1.replace('+','_')
        res1=res1.replace('/','-div-')
        res1=res1.replace(' ','')
        res2=request.POST['textfield2']
        res2=res2.replace('^','~')
        res2=res2.replace('+','_')
        res2=res2.replace('/','-div-')
        res2=res2.replace(' ','')
        return  redirect('/solve-{}-by-{}/'.format(res1,res2))
    else:
        return render(request, "Polynomials/remainder-theorem-calculator.html")


def remainder_theorem_detail(request,num1,num2):
    try:
        num1=num1.replace('~','^')
        num1=num1.replace('_','+')
        num1=num1.replace('-div-','/')
        num2=num2.replace('~','^')
        num2=num2.replace('_','+')
        num2=num2.replace('-div-','/')
        try:
            if (num1) != (request.POST['textfield1']) or (num2) != (request.POST['textfield2']):
                res1=request.POST['textfield1']
                res1=res1.replace('^','~')
                res1=res1.replace('+','_')
                res1=res1.replace('/','-div-')
                res1=res1.replace(' ','')
                res2=request.POST['textfield2']
                res2=res2.replace('^','~')
                res2=res2.replace('+','_')
                res2=res2.replace('/','-div-')
                res2=res2.replace(' ','')
                return  redirect('/solve-{}-by-{}/'.format(res1,res2))
            else:
                eval('s_p')
        except:
            if poly_remainer_db.objects.filter(inputEnter=num1+' $ '+num2).exists():
                db=poly_remainer_db.objects.filter(inputEnter=num1+' $ '+num2)
                s=[0,0]
                s[0]=db[0].detailStep
                s[1]=db[0].finalAnswer
            else:
                s=poly_remainder_func(num1,num2)
                b=poly_remainer_db(inputEnter=num1+' $ '+num2,detailStep=s[0],finalAnswer=s[1],slug='/solve-{}-by-{}/'.format(num1.replace('^','~').replace('+','_').replace('/','-div-'),num2.replace('^','~').replace('+','_').replace('/','-div-')),solutionTitle='solve {} by {}'.format(num1,num2),date_modified=date.today())
                b.save()
            num1=num1.replace('-by-','/')
            num2=num2.replace('-by-','/')
            return render(request, 'Polynomials/poly_remainder_detail.html',{'input1':num2,'s':s[0],'input':num1,'result':s[1]})
    except Exception as e:
        print(e)
        return redirect('/remainder-theorem-calculator/')
