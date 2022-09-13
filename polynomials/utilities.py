from sympy.abc import *
from latex2sympy.process_latex import process_sympy
from mpmath import *
from sympy import *
from sympy import latex
import sympy
def prime_factors(n):
            i = 2
            factors = []
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors.append(str(i))
            if n > 1:
                factors.append(str(n))
            return factors
#evaluate expression using provided values
def round_func1(n,n1):
        if float(int(float(n)))==float(n):
            return round(float(n))
        else:
            return round(float(n),n1) 
def poly_Evaluation_func(x):
    v=[]
    a=v.append
    l=x.split(',')
    #process_sympy is used to convert latex to sympy expression
    l[0]=str(process_sympy(l[0])).replace(' ','')
    l1=l[1].split('=')
    l1[1]='('+l1[1]+')'
    #'s' is the replacement of expression with it's value
    s=l[0].replace(l1[0],l1[1])
    #'t' is spliting the expression 's'
    t=sympify(s,evaluate=False).args
    l2=[]
    #used to evaluate each expression
    if '+' in s[1:] or '-' in s[1:]:
        for i in t:
            l2.append(str(eval(str(i))))
        l3=[l2[0]]
        #for use for adding '+' or '-' before the terms
        for i in range(1,len(l2)):
            if l2[i].startswith('-')==False:
                l3.append('+'+l2[i])
            else:
                l3.append(l2[i])
        #'s1' is to combine the terms
        s1=''.join(l3)
        #'ls' is the final answer after symplification
        ls=str(sympify(s1))
        poly=x.split(',')
        a('<p>Given Polynomial is {} .</p>'.format(poly[0]))
        
        #latex(sympify(s,evaluate=False)) is used to convert expression to latex format
        
        k=list(simplify(process_sympy(poly[0])).args)
        
        k=[str(i) for i in k]
        k=['('+i.replace('**','^').replace('*','.')+')' for i in k]
        k1=list(simplify(process_sympy(poly[0])).args)
        a('<p>= {}</p>'.format('+'.join(k)))
        a('<p>By putting {} = {} we can rewrite it as </p>'.format(l1[0],l1[1]))
        a('<p>= {}</p>'.format('+'.join(k).replace(l1[0],str(l1[1]))))
        p=[]
        for i in k1:
            p.append('('+str(simplify(str(i).replace(l1[0],l1[1])))+')')
        #a('<p>{}</p>'.format(str(sympify(s,evaluate=False))).replace('*',' <span>&#183;</span> '))
        a('<p>= {}</p>'.format('+'.join(p)))
        #a('<p>= {}</p>'.format(str(sympify(s1,evaluate=False)).replace('*',' <span>&#183;</span> ')))
        if '.' in str(sympify(ls,evaluate=False)):
            a('<p>= {}</p>'.format(round(sympify(ls,evaluate=False),4)))
        else:
            a('<p>= {}</p>'.format(sympify(ls,evaluate=False)))
    else:
        a('<p>Given Polynomial is {} .</p>'.format(str(x).replace('*',' <span>&#183;</span> ')))
        a('<p>By putting {} = {} we can rewrite it as </p>'.format(l1[0],l1[1]))
        a('<p>='+str(sympify(s,evaluate=False))+'</p>')
        a('<p>='+str(simplify(s))+'</p>')
        ls=str(simplify(s))
    detailstep=''.join(v)
    detailsteps=detailstep.replace('*','<span>&#215;</span>')
    return detailsteps,round_func1(ls,4)
#write polynomials in descending order
def poly_ascending_func(x):
    v=[]
    a=v.append
    y=str(process_sympy(x)).replace(' ','')
    y=str(sympify(y))
    z=sympify(y,evaluate=False).args
    l=[]
    # after splitting the expressions converting that to latex 
    for i in z:
        if str(i).startswith('-'):
            l.append(str(i).replace('**','^').replace('*',''))
        else:
            l.append('+'+latex(sympify(str(i),evaluate=False)))
    #made the list reverse and store in l1 and join that
    l1=l[::-1]
    sk=''.join(l1)
    if sk.startswith('+'):
        sk=sk[1:]
    a('The Given Polynomial is ${}$<br>'.format(latex(x)))
    a('The ascending Order of polynimial is ${}$'.format(sk))
    return ''.join(v).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),sk.replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\left(','(').replace('\\right)',')')
#write polynomial in descending order
def poly_descending_func(x):
    v=[]
    a=v.append
    y=str(process_sympy(x)).replace(' ','')
    y=str(sympify(y))
    a('The Given Polynomial is ${}$<br>'.format(latex(x)))
    a('The descending Order of polynimial is ${}$'.format(latex(sympify(y,evaluate=False))))
    return ''.join(v).replace('\\left(','(').replace('\\right)',')').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),latex(sympify(y,evaluate=False)).replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','')
#addiion of polynomials
def poly_addition_func(x):
    v=[]
    a=v.append
    y=str(process_sympy(x)).replace(' ','')
    a('<p>The given Expression is {}</p>'.format(x))
    a('<p>After grouping  similar terms we get {}</p>'.format(latex(sympify(y,evaluate=False))))
    s=combine_term_func(x)
    print(s)
    return ''.join(v).replace('\\left(','(').replace('\\right)',')').replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','')+s[0],s[1].replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('\\left(','(').replace('\\right)',')').replace('}','').replace('{','')
def poly_substraction_func(x):
    v=[]
    a=v.append
    sa1=x
    #removing all \left,\right generated by latex
    x=x.replace(r'\left','')
    x=x.replace(r'\right','')
    l=x.split(')-(')
    l=x.split(')-(')
    l[0]=l[0].replace('(','')
    l[-1]=l[-1].replace(')','')
    l1=[]
    for i in range(len(l)):
        l[i]=str(process_sympy(l[i])).replace(' ','')
    #Removing brackets and expand the expression
    for i in l[1:]:
        l1.append(str(sympify('-('+(i)+')')))
    for i in l1:
        if i.startswith('-')==False:
            l1[l1.index(i)]='+'+i
    if i.startswith('-')==False:
        s1=l[0]+'+'+''.join(l1)
    else:
        s1=l[0]+''.join(l1)
    ss=combine_term_func(latex(sympify(s1,evaluate=False)).replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('\\left(','(').replace('\\right)',')').replace('}{','/').replace('}','').replace('{',''))
    s1=s1.replace('**','^')
    a('<p>The given Expression is ${}$</p>'.format(sa1))
    a('<p>After removing all the brackets this expression can be written as ${}$.</p>'.format(s1))
    a('<p>After grouping  similar terms we get ${}$</p>'.format(latex(sympify(s1,evaluate=False))))    
    return ''.join(v).replace('\\left(','(').replace('\\right)',')').replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('++','+').replace('+ -','-')+ss[0],ss[1].replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('\\left(','(').replace('\\right)',')').replace('}{','/').replace('}','').replace('{','')
#multiplication of polynomials  
def poly_multiplication_func1(x):
    v=[]
    a=v.append
    y=str(process_sympy(x)).replace(' ','')
    #spliting terms to find the all multiplyer
    n1=sympify(y,evaluate=False).args
    n=[]
    nt=[]
    for i in n1:
        n.append(str(sympify(str(i))))
        nt.append(str(sympify(str(i))))
    sing=[]
    for i in nt:
        if i[0]=='-' and '+' not in i and '-' not in i[1:]:
            sing.append(i)
            n.remove(i)
        elif '+' not in i and '-' not in i[1:]:
            sing.append(i)
            n.remove(i)
        elif len(i)==1:
            sing.append(i)
            n.remove(i)
    #if length > 2 follow poly_multiplication function otherwise polymu function
    if len(n) > 2:
        x1=''
        # joi multiplyer with '*'
        for i in n:
            x1=x1+'*('+i+')'
        x1=x1[1:]
        z=poly_multiplication_func(x1)
        x2=z[0]
        st1=z[1]
        ss=z[2]
        st2=z[3]
        a('<p>{}</p>'.format(st1))
        for i,j in x2:
            a('<p>={}</p>'.format(i))
            a('<p>={}</p>'.format(j))
        a('<p>={}</p>'.format(ss))
        a('<p>={}</p>'.format(st2))
        if len(sing)>1 or len(sing)==1:
            mult=1
            for i in sing:
                mult=simplify(mult*sympify(i))
            a('<p>({}){}</p>'.format(latex(mult),st1))
            for i,j in x2:
                a('<p>='+latex(mult)+'{}</p>'.format(i))
                a('<p>=$'+latex(mult)+'{}</p>'.format(j))
            a('<p>='+latex(mult)+'{}</p>'.format(ss))
            a('<p>=('+latex(mult)+')({})</p>'.format(st2))
            a('<p>={}</p>'.format(latex(expand(mult*process_sympy(st2)))))
        else:
            a('<p>{}</p>'.format(st1))
            for i,j in x2:
                a('<p>={}</p>'.format(i))
                a('<p>={}</p>'.format(j))
            a('<p>={}</p>'.format(ss))
            a('<p>={}</p>'.format(st2))
        return ''.join(v).replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),st2
    else:
        if  len(sing)>1:
            mult=1
            for i in sing:
                mult=simplify(mult*sympify(i))
            a('<p>{}={}</p>'.format(x,latex(expand(mult*sympify(n[0])))))
            return ''.join(v).replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),latex(expand(mult*sympify(n[0])))
        else:
            z=polymul(str(n[0]),str(n[1]))
            st1=x
            ss=z[0]
            st2=z[1]
            a('<p>{}</p>'.format(st1))
            #Removing unnecessary \left and \right generating by latex function
            a('<p>={}</p>'.format(latex(sympify(ss,evaluate=False)).replace('\\left','').replace('\\right','')))
            #using list compression
            st=[str(latex(i).replace('\\left','').replace('\\right','')) for i in list(sympify(st2,evaluate=False).args)]
            a('<p>={}</p>'.format(latex('+'.join(st)).replace('\\left','').replace('\\right','')))
            a('<p>={}</p>'.format(latex(sympify(st2)).replace('\\left','').replace('\\right','')))
            return ''.join(v).replace('\\left(','(').replace('\\right)',')').replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),latex(sympify(st2)).replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('\\left(','(').replace('\\right)',')').replace('}{','/').replace('}','').replace('{','')
#finding degree of polynomials 
def degree_pol_func(x):
    v=[]
    a=v.append
    a('<p>The given expression is ${}$</p>'.format(x))
    x=str(process_sympy(x))
    a=v.append
    #total_degree is a sympy function used for finding degree of the whole expression 
    z=str(total_degree(poly(x)))
    l=[]
    t1=sympify(x,evaluate=False).args
    for i in t1:
        try:
            #degree_list is the function to fnd degree of indivisual expression having more variables
            l.append(str(list(degree_list(i)))[1:-1])
        except Exception:
            if isinstance(i, Integer)==True:
                l.append(0)
        except:
            l.append(str(degree(i)))
            l.append(0)
    zip_file=zip(l,list(t1))
    a('<ul>')
    for i,j in zip_file:
                a('<li>The degree of ${}$ is {}</li>'.format(latex(j),i))
    a('</ul>')
    a('<p>But the degree of  expression  will the highest degree of the indivisual expression of above i.e  {}</p>'.format(z))
    return ''.join(v).replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\left','').replace('\\right',''),z
#combine_term_func() combines all the similar terms of a polynomial
def combine_term_func(x):
    v=[]
    a=v.append
    #a('<p>The given term is {}</p>'.format(x))
    y1=process_sympy(x)
    #spliting all expressions into terms
    y=sympify(str(y1),evaluate=False).args
    l=[]
    for i in y:
        l.append(i)
    l1=[]
    l2=[]
    l3=[]
    for i in l:
        try:
            
            if isinstance(i,Rational)==True:
                    l2.append(str(i))
            elif isinstance(i,Integer)==True:
                    l2.append(str(i))
            else:
                #LM will find the variables in the expression
                l1.append(str(LM(LM(i))))
                l3.append(str(i))
        except:
            #Mul is a sympy class
            if isinstance(i,Mul)==True:
                l2.append(str(i))
    z=list(set(l1))
    l6=[]
    l=[str(i) for i in l]
    for i in z:
        lk=[]
        for j in l3:
            if LM(i)==LM(j):
                # converting to latex and store in lk
                lk.append(latex(sympify(j,evaluate=False)).replace('\\left(','(').replace('\\right)',')').replace(r'frac{-1','frac{-'))
            else:
                continue
        l6.append(lk)
    zip_file=zip(z,l6)
    m=latex(sympify(y1,evaluate=False))
    m=m.replace('\\left','')
    m=m.replace('\\right','')
    m=m.replace('(','')
    m=m.replace(')','')
    m=m.replace('frac{-1','frac{-')
    a('<p>After combining similar terms we get ${}$</p>'.format(m))
    for i,j in zip_file:
        if len(j) >=2:
            j=','.join(j)
            a('<p>${}$ has similar terms {}</p>'.format(latex(sympify(i,evaluate=False)),j))
        else:
            s=str(j)[2:-2].replace('$','')
            s=s.replace(r'\\frac',r'\frac')
            t=latex(process_sympy(s))
            t=t.replace('\\left','')
            t=t.replace('\\right','')
            t=t.replace('(','')
            t=t.replace(')','')
            t=t.replace('frac{-1','frac{-')
            a('<p>${}$ has similar terms ${}$</p>'.format(latex(sympify(i,evaluate=False)),t))
    a('<p>By adding all the similar terms we get ${}$</p>'.format(latex(simplify(process_sympy(m)))))
    return ''.join(v).replace('\\left(','(').replace('\\right)',')').replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('+ -','-'),latex(simplify(process_sympy(m)))
#leading_func() finds the leading terms of a polynomial
def leading_func(x):
    v1=[]
    a=v1.append
    x1=process_sympy(x)
    print(x)
    print(x1)
    x1=simplify(x1)
    
    t1=sympify(x1,evaluate=False).args
    print(t1,'term')
    z=[]
    for i in t1:
        z.append(str(i))
    l2=[]
    print(z,'terms')
    #appending degree of indivisual terms
    for i in t1:
        if isinstance(i, Integer)==True:
            l2.append(0)
        else:
            try:
                l2.append(int(str(total_degree(i))))
            except:
                l2.append(0)
    print(l2,'degree')
    l3=[]
    v=max(l2)
    print(v,'max')
    #compare with index to find the index having highest degree
    for i in range(0, len(l2)) : 
        if l2[i] == v : 
            l3.append(i) 
    zip_file=zip(l2,z)
    l4=[]
    #finding highest degree terms
    for i in l3:
        l4.append(z[i])
    l=[]
    l1=[]
    for i in l4:
        l.append(str(sympify(i)))
        l1.append(str(LC(i)))
    l5=[]
    l6=[]
    for i in l4:
        #symplifying terms
        if str(sympify(i))!= i:
            l5.append(i)
            l6.append(str(sympify(i)))
        l4[l4.index(i)]=latex(sympify(i,evaluate=False))
    o=zip(l5,l6)
    m=zip(l,l1)
    a('<p>The given input is {}</p>'.format(x))
    a('<p>The term can be simplified as {}</p>'.format(latex(sympify(x1,evaluate=False))))
    for i,j in zip_file:
        a('<p>-- ${}$ term has  degree {} . </p>'.format(latex(sympify(j,evaluate=False)),i))
        #print('<p>-- ${}$ term has  degree {} . </p>'.format(latex(j),i))
        a('<br>')
    a('<p>--Here highest degree is maximum of all degrees of terms i.e {} .</p>'.format(v))
    a('<br>')
    a('<p>--Hence the leading term of the polynomial will be the terms having highest degree i.e ${}$ .<br></p>'.format(latex(sympify(str(l4)[1:-1],evaluate=False))))
    for i,j in o:
        a('<p>--${}$ can be symplified as ${}$ .</br></p>'.format(latex(sympify(i,evaluate=False)),latex(sympify(j,evaluate=False))))
        a('<br>')
    for i,j in m:
        a('<p>--${}$ has coefficient ${}$ .</br></p>'.format(latex(sympify(i,evaluate=False)),j))
        a('<br>')
    print(str(l4)[1:-1].replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''))
    return ''.join(v1).replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\left(','(').replace('\\right)',')'),[str(l4)[1:-1].replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\left','').replace('\\right','').replace('\\',''),str(l1)[1:-1].replace('\\','')]
#num_perfect_sqr_func() finds the perfect square numbers
def num_perfect_sqr_func(x):
    v=[]
    a=v.append
    s=sqrt(int(str(sympify(x))))
    #comparing sqrt with aprox near whole number
    if float(int(s))==s:
        s=int(s)
        a('A perfect square number is an integer that is the square of another integer.')
        a('<br>')
        a('$\\sqrt{%s}= %s $'%(x,s))
        a('<br>')
        k='Here the square root is a perfect integer. So it is a Perfect square.'
        a(k)
    else:
        s=sqrt(float(str(sympify(x))))
        a('A perfect square number is an integer that is the square of another integer.')
        a('<br>')
        a('$\\sqrt{%s}= %s $'%(x,s))
        a('<br>')
        k='Here the square root is not an Integer. So it is not a Perfect square.'
        a(k)
    return ''.join(v),k
#Ckeck for an Expression is polynomial or not
def compare_expr_func(x):
        v=[]
        a=v.append
        res1 = x
        res1 = str(process_sympy(res1)).replace(' ','')
        result=sympify(res1)
        a('<p>The expression can be written as {} </p>'.format(latex(result)))
        a('<p>polynomial is a combination of terms separated using + or − signs. Polynomials cannot contain any of the following: </p>')
        a('<p>i)Variables raised to a negative or fractional exponent. </p>')
        a('<p>i)Variables in the denominator. </p>')
        a('<p>iii)Variables under a radical.  </p>')
        a('<p>iv)Special features. (trig functions, absolute values, logarithms, … ). </p>')
        res1=str(result)
        if '**(' in res1.replace(' ',''): 
            k='<p>{} is not a polynomial.</p>'.format(x)
            a(k)
        else:
            k='<p>{} is  a polynomial.</p>'.format(x)
            a(k)
        return ''.join(v).replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),k.replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('<p>','').replace('</p>','')
def polymul(x,y):
        if x.find('+') or x.find('-'):
            t=sympify(x,evaluate=False).args
            l=[]
            for i in t:
                l.append(str(i))
        l1=[]
        for i in l:
            l1.append('('+i+')*('+y+')')
        x3='+'.join(l1)
        if y.find('+') or y.find('-'):
            t1=sympify(y,evaluate=False).args
            l1=[]
            for i in t1:
                l1.append(str(i))
            l2=[]
            for j in l1:
                for k in l:
                    l2.append('('+k+')*('+j+')')
        x4='+'.join(l2)
        l5=[x3,x4]
        return l5  
def poly_multiplication_func(x):
    try:
        s=sympify(x,evaluate=False).args
        l=[]
        l3=[]
        l4=[]
        for i in s:
            l.append('('+str(i)+')')
    except:
        l3=[]
        l4=[]
        l=x.split(')(')
        l1=x.split(')(')
        l[0]=l[0]+')'
        l[-1]='('+l[-1]
        l1[0]=l[0]+')'
        l1[-1]='('+l[-1]
        for i in l1:
            l[l1.index(i)]=i.replace(')','').replace('(','')
            l[l1.index(i)]='('+l[l1.index(i)]+')'
    z=polymul(l[0],l[1])
    
    l3.append('('+z[0]+')*'+'*'.join(l[2:]))
    l4.append('('+z[1]+')*'+'*'.join(l[2:]))
    for i in range(2,len(l)):
        z=str(sympify(z[1]))
        z=polymul(z,l[i])
        if l[i+1:]:
            l3.append('('+z[0]+')*'+'*'.join(l[i+1:]))
            l4.append('('+z[1]+')*'+'*'.join(l[i+1:]))
        else:
            l3.append('('+z[0]+')')
            l4.append('('+z[1]+')')
    z1=sympify(l4[-1],evaluate=False).args
    l5=[]
    for i in z1:
        l5.append('('+str(simplify(i))+')')
    sk='+'.join(l5)
    z2=simplify(sk)
    st=str(z2).replace('**','^')
    st2=st.replace('*','')
    sss=sk.replace('**','^')
    ss=sss.replace('*','')
    l2=[]
    l6=[]
    for i in l3:
        sn=i.replace('**','^')
        l2.append(sn.replace('*',''))
    for i in l4:
        sn1=i.replace('**','^')
        l6.append(sn1.replace('*',''))
    x2=zip(l2,l6)
    st=x.replace('**','^')
    st1=st.replace('*','')
    return x2,st1,ss,st2
#check for a polynomial is perfect cube
def poly_cube_func(n):
    print(n)
    v=[]
    a=v.append
    a('The given polynomial is ${}$<br>'.format(n))

    if str(process_sympy(n)).replace(' ','')==str(factor(process_sympy(n))).replace(' ',''):#for no factor
            a('It has no factors<br>.So it is not a cube')
    else:
        if str(factor(primitive(process_sympy(n))[1]).args[0]).replace(' ','')=='-1':#factoring polynomial
            z=factor(primitive(process_sympy(n))[1]).args[1].args[1]
            z1=sympify('-('+str(factor(primitive(process_sympy(n))[1]).args[1].args[0])+')')
            a('Simplifying the polynomial we get <br>${}$<br>'.format(latex(simplify(process_sympy(n)))))
            if isinstance(z/3,Integer):#check the power multiple of 3
                a('we can write this polynomial in the form of <br>$a^3+3a^2b+3ab^2+b^3$<br>')
                a1=latex(z1.args[0])
                b=latex(z1.args[1])
                a('we can write this polynomial in the form of <br>$({})^3+3({})^2({})+3({})({})^2+{}^3$<br>'.format(a1,a1,b,a1,b,b))
                a('Factoring the polynomial we Get <br>$({})^3$<br>'.format(z1))
                a('It has power i.e. multiple of 3.<br>')
                a('${}$ is a perfect Cube'.format(n))
            else:
                a('After factoring the polynomial we get <br>${}$<br>'.format(latex(factor(simplify(process_sympy(n))))))
                a('${}$ is not a perfect Cube'.format(n))
        else:
            z=factor(primitive(process_sympy(n))[1]).args[1]
            z1=factor(primitive(process_sympy(n))[1]).args[0]
            if isinstance(z/3,Integer):#check the power multiple of 3
                a('we can write this polynomial in the form of <br>$a^3+3a^2b+3ab^2+b^3$<br>')
                a1=latex(z1.args[0])
                b=latex(z1.args[1])
                a('we can write this polynomial in the form of <br>$({})^3+3({})^2({})+3({})({})^2+{}^3$<br>'.format(a1,a1,b,a1,b,b))
                a('Factoring the polynomial we Get <br>$({})^3$<br>'.format(z1))
                a('It has power i.e. multiple of 3.<br>')
                a('${}$ is a perfect Cube'.format(n))
            else:
                a('After factoring the polynomial we get <br>${}$<br>'.format(latex(factor(simplify(process_sympy(n))))))
                a('${}$ is not a perfect Cube'.format(n))
    return ''.join(v),n
#polynomial division
def poly_division_func(n):
    v=[]
    a=v.append
    n1=n.split(')/(')#spliting with '/'
    n1=[i.replace(')','').replace('(','') for i in n1]
    n1=[str(simplify(process_sympy(i))).replace(' ','') for i in n1]
    s=pdiv(simplify(n1[0]),simplify(n1[1]))
    a('<p>The given expression is ${}$</p><br>'.format(n))
    a('The Divident is ${}$ and Divisor is ${}$<br><br>'.format(latex(simplify(n1[0])),latex(simplify(n1[1]))))
    sy=n1[0]
    if '+' in str(s[0]):
        s1=str(s[0]).split('+')
        s2=str(s[0]).split('+')
        for i in s1:
            if '-' in i[1:]:#condition for '-'
                ind=s2.index(i)
                i=i.replace('-','-$').replace(' ','')
                sp1=i.split('-')[::-1]
                s2.pop(ind)
                for k in sp1:
                    s2.insert(ind,k)       
    else:
        s2=str(s[0]).replace('-','-$').split('-')
    for i in s2:
        s2[s2.index(i)]=i.replace('$','-')
    l=[]
    for i in s2:
        l.append(str(expand(simplify(i+'*('+n1[1]+')'))).replace(' ',''))
    l2=[]
    for i in l:
        l2.append(str(expand('('+str(sy)+')-('+i+')')).replace(' ',''))
        sy=expand('('+str(sy)+')-('+i+')')
    a('$'+latex(simplify(n1[1]))+'$$)$$'+latex(sympify(n1[0]))+'$'+'$($$'+latex(s[0])+'$<br>')
    length=len(latex(simplify(n1[1])))
    l=[-1*simplify(i) for i in l]
    for i,j in zip(l,l2):
        a('&emsp;'*length+'$'+latex(expand(i))+'$<br><br>')
        a('&emsp;'*length+'-'*len(latex(expand(i)))+'<br>')
        length=length+1
        a('&emsp;'*length+'$'+latex(expand(j))+'$<br><br>')
    a('<p>After the division the quotient is ${}$ and reminder is ${}$</p>'.format(latex(s[0]),latex(s[1])))
    return ''.join(v).replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),[latex(s[0]).replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),latex(s[1]).replace('\\cdot','*').replace('$','').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','')]
#find polynomial gcf
def poly_gcf_func(x):
    v=[]
    a=v.append
    l=x.split(',')
    l2=x.split(',')
    for i in range(len(l)):
        l[i]=str(process_sympy(l[i])).replace(' ','')
    l1=[]
    #after spliting with ',' replace spaces with nothing and find factor for each indivisual expressions
    for i in l:
        l1.append(factor(i))
    z=zip(l2,l1)
    #find gcf and factorize gcf
    g=gcd(l)
    k=factor(g)
    a('<p>The given input is {}</p>'.format(x))
    for i,j in z:
        a('<p>${}$ has factors i.e ${}$</p>'.format(i,latex(j)))
    a('<p>By verifying each polynomial factor we get the GCF i.e common factor of the polynomial is ${}$ and simplified as ${}$</p>'.format(latex(k),latex(g)))
    return ''.join(v).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),latex(g).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','')
def poly_gcf_func1(x):
    v=[]
    a=v.append
    l=x.split(',')
    l2=x.split(',')
    for i in range(len(l)):
        l[i]=str(process_sympy(l[i])).replace(' ','')
    l1=[]
    #after spliting with ',' replace spaces with nothing and find factor for each indivisual expressions
    for i in l:
        l1.append(factor(i))
    z=zip(l2,l1)
    #find gcf and factorize gcf
    g=gcd(l)
    k=factor(g)
    a('<p>The given input is {}</p>'.format(x))
    for i,j in z:
        a('<p>${}$ has factors i.e ${}$</p>'.format(i,latex(j)))
    
    a('<p>By verifying each polynomial factor we get the GCF i.e common factor of the polynomial is ${}$ and simplified as ${}$</p>'.format(latex(k),latex(g)))
    a('<p>Factor form of GCF is ${}$ </p>'.format(latex(k)))
    return ''.join(v).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),latex(k).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','')

def poly_expand_binomial_theorm_func(x):
    v=[]
    x=process_sympy(x)
    a=v.append
    #spliting each expression
    y=list(sympify(x,evaluate=False).args)
    #condition for negative exponent
    if str(y[1]).startswith('-'):
        x1=str(y[1])
        y[1]=str(simplify('(-1)*'+str(y[1])))
        x1=x1.replace(' ','')
    else:
        x1=str(int(y[1]))
    #split the first expression in  y
    z=sympify(y[0],evaluate=False).args
    l=[]
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    l6=[]
    #generate detailed code in latex for step by implementations using expansion formula
    for i in range(int(str(y[1]))+1):
        l.append('\\frac{'+str(y[1])+'!}'+'{('+str(y[1])+'-'+str(i)+')!'+str(i)+'!}('+str(z[0])+')^{'+str(y[1])+'-'+str(i)+'}'+'\\times{}('+str(z[1])+')^'+str(i))
        l1.append('\\frac{'+str(int(rf(1,int(y[1]))))+'}'+'{('+str(int(rf(1,int(y[1])-i)))+')'+str(int(rf(1,i)))+'}('+str(z[0])+')^{'+str(y[1])+'-'+str(i)+'}'+'\\times{}('+str(z[1])+')^'+str(i))
        l2.append(str(int(int(rf(1,int(y[1])))/int(rf(1,int(y[1])-i))/(int(rf(1,i)))))+'('+str(z[0])+')^{'+str(y[1])+'-'+str(i)+'}'+'\\times{}('+str(z[1])+')^'+str(i))
        k=int(int(rf(1,int(y[1])))/int(rf(1,int(y[1])-i))/(int(rf(1,i))))
        if k==1:
            k=''
            l3.append('('+str(z[0])+')^{'+str(y[1])+'-'+str(i)+'}'+'\\times{}('+str(z[1])+')^'+str(i))
        else:
            k='('+str(k)+')'
            l3.append(k+'('+str(z[0])+')^{'+str(y[1])+'-'+str(i)+'}'+'\\times{}('+str(z[1])+')^'+str(i))
        l4.append(k+'('+str(z[0])+')^{'+str(int((y[1]))-i)+'}'+'\\times{}('+str(z[1])+')^'+str(i))
        k1=int((y[1]))-i
        l6.append(k+str(simplify('('+str(z[0])+')**'+str(k1)))+'\\times{}('+str(simplify('('+str(z[1])+')**'+str(i)))+')')
        if k1==0:
            l5.append(k+'1'+'\\times{}('+str(z[1])+')^'+str(i))
        else:
            l5.append(k+'('+str(z[0])+')^{'+str(int((y[1]))-i)+'}'+'\\times{}('+str(z[1])+')^'+str(i))
    l5[0]=k+'('+str(z[0])+')^{'+str(y[1])+'}'+'\\times{}'+'1'
    #converting sympy expression to latex
    for i in range(len(l)):
        l[i]=l[i].replace('**','^')
        l[i]=l[i].replace('*','.')
    for i in range(len(l1)):
        l1[i]=l1[i].replace('**','^')
        l1[i]=l1[i].replace('*','.')
    for i in range(len(l2)):
        l2[i]=l2[i].replace('**','^')
        l2[i]=l2[i].replace('*','.')
    for i in range(len(l3)):
        l3[i]=l3[i].replace('**','^')
        l3[i]=l3[i].replace('*','.')
    for i in range(len(l4)):
        l4[i]=l4[i].replace('**','^')
        l4[i]=l4[i].replace('*','.')
    for i in range(len(l5)):
        l5[i]=l5[i].replace('**','^')
        l5[i]=l5[i].replace('*','.')
    for i in range(len(l6)):
        l6[i]=l6[i].replace('**','^')
        l6[i]=l6[i].replace('*','.')
    y1=str(y[0])
    y2=str(y[1])
    z1=str(z[0])
    z2=str(z[1])
    lk8=str(expand(x))
    y1=y1.replace('**','^')
    y1=y1.replace('*','.')
    y2=y2.replace('**','^')
    y2=y2.replace('*','.')
    z1=z1.replace('**','^')
    z1=z1.replace('*','.')
    z2=z2.replace('**','^')
    z2=z2.replace('*','.')
    lk8=lk8.replace('**','^')
    lk8=lk8.replace('*','')
    #joining expressions
    if x1.startswith('-'):
        lk='\\frac{1}{'+'+'.join(l)+'}'
        lk1='\\frac{1}{'+'+'.join(l1)+'}'
        lk3='\\frac{1}{'+'+'.join(l2)+'}'
        lk4='\\frac{1}{'+'+'.join(l3)+'}'
        lk5='\\frac{1}{'+'+'.join(l4)+'}'
        lk6='\\frac{1}{'+'+'.join(l5)+'}'
        lk7='\\frac{1}{'+'+'.join(l6)+'}'
        st='(a+b)^{-n} =\\frac{1}{(a+b)^{n}}'
    else:
        lk='+'.join(l)
        lk1='+'.join(l1)
        lk3='+'.join(l2)
        lk4='+'.join(l3)
        lk5='+'.join(l4)
        lk6='+'.join(l5)
        lk7='+'.join(l6)
        st=''
    a('<div class="binomial1"><p class="binomial">$${}$$</p>'.format(st))
    a('<p class="binomial">According to the binomial formula $(a+b)^n$ = $\\sum_{k=0}^{n} {^nC_k}(a^{n-k}b^{k})$</p>')
    a('<p class="binomial">So $(%s)^%s$ = $\\sum_{k=0}^%s {^%sC_k}((%s)^{%s-k}(%s)^{k})$</p>'%(y1,y2,y2,y2,z1,y2,z2))
    a('<p class="binomial">By expanding the summation:</p>')
    a('<p class="binomial">${}$</p>'.format(lk))
    a('<p class="binomial">$= {}$</p>'.format(lk1))
    a('<p class="binomial">$= {}$</p>'.format(lk3))
    a('<p class="binomial">$= {}$</p>'.format(lk4))
    a('<p class="binomial">$= {}$</p>'.format(lk5))
    a('<p class="binomial">$= {}$</p>'.format(lk6))
    a('<p class="binomial">$= {}$</p>'.format(lk7))
    a('<p class="binomial">$= {}$</p></div>'.format(lk8))
    return ''.join(v).replace('$$$$</p>',''),lk8
#finding lcm of polynomial
def poly_lcm_using_gcf_func(x):
    v=[]
    a=v.append
    y=x.split(',')
    y1=[]
    for i in y:
        y1.append('('+i+')')
    #converting each expression into sympy expression
    y=[str(process_sympy(i)).replace(' ','') for i in y]
    k1='\\times{}'.join(y1)
    g=gcd(y)
    #convert to poly object of sympy for doing multilpication operation
    z=Poly(y[0])
    for i in y[1:]:
        z=z.mul(Poly(i))
    k=str(z.args[0])
    l2=[]
    #dividing gcd have power total (terms-1) from total multiplication of all terms
    for i in y:
        n=str(factor(i))
        n=n.replace('**','^')
        n=n.replace('*','\\times{}')
        l2.append(n)
    s=len(y)
    s1=g**(s-1)
    s2=div(k,s1)
    lcm=str((s2)[0])
    lcm=lcm.replace('**','^')
    lcm=lcm.replace('*','')
    g=str(g).replace('**','^')
    g=g.replace('*','\\times{}')
    x=x.replace('**','^')
    x=x.replace('*','\\times{}')
    s1=str(s1).replace('**','^')
    s1=s1.replace('*','\\times{}')
    k=k.replace('**','^')
    k=k.replace('*','\\times{}')
    k1=k1.replace('**','^')
    k1=k1.replace('*','\\times{}')
    z1=x.split(',')
    a('<p>The given Expressions are ${}$</p>'.format(x))
    for i,j in zip(z1,l2):
        a('<p>$%s$ has factors i.e $%s$</p>'%(i,j))
    a('<p>By finding the GCF of given expressions we get that the gcf is $%s$</p>'%(g))
    a('<p>There are $%s$ number of expressions are given.</p>'%(s))
    a('<p>To find the LCM we have to first multiply all the expressions $%s$ = $%s$</p>'%(k1,k))
    a('<p>To find the LCM we have devide $%s-1$ power of gcf from $%s$</p>'%(s,k))
    a('<p>So by dividing $%s$ from $%s$ = $(%s)/(%s)$ =   $%s$</p>'%(s1,k,k,s1,lcm))
    a('<p>So the LCM of $%s$ is $%s$</p>'%(x,lcm))
    return ''.join(v).replace('\\times{}','').replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),lcm.replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}','')
#determine if a polynomial is prime or not
def poly_prime_soln_func(x):
    v=[]
    a=v.append
    x=str(process_sympy(x)).replace(' ','')
    #finding factors
    y=str(factor(x))
    y=y.replace(' ','')
    #comparing factors
    if str(sympify(x)).replace(' ','')==y:
        k='It is a prime polynomial because it has only two factors i.e 1 and '+'$'+latex(sympify(y,evaluate=False))+'$'
    else:
        
        z=sympify(y,evaluate=False).args
        l=[]
        for i in z:
            l.append('$'+latex(i)+'$')
        l1=set(l)
        l=list(l1)
        n=','.join(l)
        k='It is not a Prime Polynomial due to it has more than 2 factors like 1,'+n+','+'$'+latex(sympify(x,evaluate=False))+'$'
    a('<p>The given polynomial is ${}$</p>'.format(latex(sympify(x,evaluate=False))))
    a('<p>So ${}$  =  ${}$</p>'.format(latex(sympify(x,evaluate=False)),latex(sympify(y,evaluate=False))))
    a('<p>{}</p>'.format(k))
    return ''.join(v).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}',''),k.replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}','')
#factorization over complex number
def poly_factor_over_complex1_func(x):
    v=[]
    a=v.append
    com=x
    x=str(process_sympy(x)).replace(' ','')
    x=x.replace('i','I')
    #factor over complex number 'I' 
    y=factor(x, extension=[I])
    if str(simplify(process_sympy(x)))==factor(str(y), extension=[I]):
        a("<p>${}$ has no factors over complex root</p>".format(com))
        return v[0],com
    #spliting each factors
    y1=sympify(y,evaluate=False).args
    l=[]
    l1=[]
    for i in y1:
        l1.append(str(i).replace(' ',''))
    for i in range(len(l1)):
        try:
            if isinstance(eval(str(l1[i]).replace('I','i')),int):
                for j in range(eval(str(i))):
                        l.append(l[i-1])
        except:
                l.append(l1[i].replace(' ',''))
    for i in range(len(l)):
        if l[i]==str(expand(l[i])).replace(' ',''):
            l[i]=l[i]
        else:
            s2=factor(l[i])
            s1=sympify(s2,evaluate=False).args
            for j in s1:
                try:
                    if type(eval(str(j)))==int:
                        l.insert(i,l[i])
                except Exception as E:
                        E
                        l.pop(i)
                        k=str(j).replace(' ','')
                        l.insert(i,k)     
    # using multiplication methods of polynomial generated intermediate steps        
    for i in l:
        l[l.index(i)]='('+i+')'
    if len(l)==2:
        s3=polymul(l[0],l[1])
        k1=zip([],[])
        k2=s3[0].replace('**','^')
        k2=k2.replace('*','\\times{}')
        k3=s3[1].replace('**','^')
        k3=k3.replace('*','\\times{}')
        k4=x.replace('**','^')
        k4=k4.replace('*','')
        k5=str(y).replace('**','^')
        k5=k5.replace('*','')
    else:
        s3=poly_multiplication_func('*'.join(l))
        k1=s3[0]
        k1=list(zip(*k1))
        k1=zip(list(k1[1])[::-1],list(k1[0])[::-1])
        k2=s3[1]
        k3=s3[2]
        k4=s3[3]
        k5=''
    a('<p>$={}$</p>'.format(k4))
    a('<p>$={}$</p>'.format(k3))
    for i,j in k1:
        a('<p>$={}$</p>'.format(i))
        a('<p>$={}$</p>'.format(j))
    a('<p>$={}$</p>'.format(k2))
    a('<p>$={}$</p>'.format(k5))
    return ''.join(v).replace('$','').replace('I','i').replace('\\times','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}',''),k5.replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}','').replace('\\times','').replace('I','i')
import math
from sympy import gcd
def quad_equation_func(num1):
    s1=num1.split('=')
    s1=[str(process_sympy(i)) for i in s1 ]
    s1=s1[0]+'+('+str(sympify('-('+s1[1]+')'))+')'
    s1=sympify(str(s1))
    sk=sympify(str(s1),evaluate=False).args
    s1=sympify(s1)/LC(sk[0])#convert to symplify format
    s2=sympify(s1)
    s3=sympify(str(s2),evaluate=False).args
    s4=LC(s3[0])
    s22=sympify(str(s3[0])+'+'+str(s3[1]))
    s22_divide=(s22)/s4
    b=LC(s3[1]/s4)
    b1=b/2#need to add both sides for squaring
    s22_add=s22_divide+b1
    n1=sympify('-'+str(s3[2]))/s4
    n2=latex(n1)+'+('+latex(b1)+')^2'
    s22_add1=latex(s22_divide)+'+('+latex(b/2)+')^2'
    n21=latex(simplify(process_sympy(n2)))
    st='('+str(LM(s3[1]))+'+'+latex(b/2)+')^2'
    st1=str(LM(s3[1]))+'+'+latex(b/2)
    n22='\\sqrt{'+n21+'}'
    v=[]
    a=v.append
    a('Given Equation is ')
    a('${}$<br><br>'.format(num1))
    a('Divide {} from every terms and shifting all terms to one part of equation<br><br>'.format(LC(sk[0])))
    a('$=>{} = 0$<br><br>'.format(latex(s2)))
    a('$=>{}$ = ${}$<br><br>'.format(latex(s22_divide),latex(n1)))
    a('Adding $('+latex(b/2)+')^2$'+'to both sides of equation<br><br>')
    a('$=>{}$ = ${}$<br><br>'.format(s22_add1,n2))
    a('We get a squaring in the left hand side<br><br>')
    a('$=>{}$ = ${}$<br><br>'.format(st,n21))
    a('$=>{}$ = ${}$<br><br>'.format(latex(process_sympy(st1)),n22))
    if process_sympy(n21)<0:
        soln1=round(math.sqrt(sympify('-'+str(process_sympy(n21)))),2)
        latex(simplify('-'+str(b))/2)
        a('$=>{}$ = <span>&#8723;</span>${}i$<br><br>'.format(latex(process_sympy(st1)),soln1))
        a('$=>{}$ = ${}i+({})$ or $-{}i+({})$<br><br>'.format(LM(s3[1]),soln1,latex(simplify('-'+str(b))/2),soln1,latex(simplify('-'+str(b))/2)))
    else:
        n222=math.sqrt(process_sympy(n21))    
        if math.sqrt(process_sympy(n21))==0.0:
            a('$=>{}$ = <span>&#8723;</span>${}$<br><br>'.format(latex(process_sympy(st1)),round(n222,2)))
            a('$=>{}$ = ${}+({})$ or $-{}+({})$<br><br>'.format(LM(s3[1]),round(n222,2),latex(simplify('-'+str(b))/2),round(n222,2),latex(simplify('-'+str(b))/2)))
            soln=sympify(str(round(n222,2))+'+'+str(simplify('-'+str(b))/2))
            a('$=>{}$ = ${}$ '.format(LM(s3[1]),round(soln)))
        else:
            a('$=>{}$ = <span>&#8723;</span>${}$<br><br>'.format(latex(process_sympy(st1)),round(n222,2)))
            a('$=>{}$ = ${}+({})$ or $-{}+({})$<br><br>'.format(LM(s3[1]),round(n222,2),latex(simplify('-'+str(b))/2),round(n222,2),latex(simplify('-'+str(b))/2)))
            soln1=sympify(str(round(n222,2))+'+'+str(simplify('-'+str(b))/2))
            soln2=sympify('-'+str(round(n222,2))+'+'+str(simplify('-'+str(b))/2))
            a('$=>{}$ = ${}$ or ${}$ = ${}$'.format(LM(s3[1]),round(soln1,2),LM(s3[1]),round(soln2,2)))
    return ''.join(v),st1
#solvig quadratic equation by formula
def quad_equation_formula_func(num1):
    s1=num1.split('=')
    s1=[str(process_sympy(i)) for i in s1 ]
    s1=s1[0]+'+('+str(sympify('-('+s1[1]+')'))+')'
    s1=sympify(str(s1))
    #sk=sympify(str(s1),evaluate=False).args
    #s1=sympify(s1)/LC(sk[0])
    s2=sympify(s1)
    s3=sympify(str(s2),evaluate=False).args
    a=LC(str(s3[0]))
    b=LC(str(s3[1]))
    c=eval(str(s3[2]))
    discriminant = (b * b) - (4 * a * c)
    v=[]
    a1=v.append
    if(discriminant > 0):#root greater than 0
        root1 = round((-b + math.sqrt(discriminant)) / (2 * a),3)
        root2 = round((-b - math.sqrt(discriminant)) /  (2 * a),3)
        a1('Given Equation is ${}$<br><br>'.format(num1))
        a1('By converting the equation into $ax^2+bx+c=0$ by simplifyinng the equation <br><br>')
        a1('$=>{} = 0$<br><br>'.format(latex(s2)))
        a1('a = {} b = {} c = {}<br><br>'.format(a,b,c))
        a1('$x$ = $\\frac{-b\pm\sqrt{b^2-4ac}}{2a}$<br><br>')
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s^2-4(%s)(%s)}}{2(%s)}$<br><br>'%(b,b,a,c,a))
        a1('Multiplyig {} with {}<br><br>'.format(a,c))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s^2-4(%s)}}{2(%s)}$<br><br>'%(b,b,a*c,a))
        a1('Multiplyig {} with 4 <br><br>'.format(a*c))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s^2-(%s)}}{2(%s)}$<br><br>'%(b,b,a*c*4,a))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s-(%s)}}{2(%s)}$<br><br>'%(b,b*b,a*c*4,a))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s}}{2(%s)}$<br><br>'%(b,discriminant,a))
        a1('$x$ = $\\frac{-(%s)\pm %s}{2(%s)}$<br><br>'%(b,math.sqrt(discriminant),a))
        a1('$x$ = $\\frac{-(%s) + %s}{2(%s)}$  or  $x$ = $\\frac{-(%s) - %s}{2(%s)}$<br><br>'%(b,math.sqrt(discriminant),a,b,math.sqrt(discriminant),a))
        a1('$x$ = $\\frac{%s}{2(%s)}$  or  $x$ = $\\frac{%s}{2(%s)}$<br><br>'%(-b + math.sqrt(discriminant),a,-b - math.sqrt(discriminant),a))
        a1('$x$ = $%.2f$  or  x = $%.2f$<br><br>'%(root1,root2))
        a1("Two Distinct Real Roots Exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
        return ''.join(v),(str(root1),str(root2))
    elif(discriminant == 0):#condition for root = 0
        root1 = root2 = -b / (2 * a)
        a1('Given Equation is ${}$<br><br>'.format(num1))
        a1('By converting the equation into $ax^2+bx+c=0$ by simplifyinng the equation <br><br>')
        a1('$=>{} = 0$<br><br>'.format(latex(s2)))
        a1('a = {} b = {} c = {}<br><br>'.format(a,b,c))
        a1('$x$ = $\\frac{-b\pm\sqrt{b^2-4ac}}{2a}$<br><br>')
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s^2-4(%s)(%s)}}{2(%s)}$<br><br>'%(b,b,a,c,a))
        a1('Multiplyig {} with {}<br><br>'.format(a,c))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s^2-4(%s)}}{2(%s)}$<br><br>'%(b,b,a*c,a))
        a1('Multiplyig {} with 4 <br><br>'.format(a*c))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s^2-(%s)}}{2(%s)}$<br><br>'%(b,b,a*c*4,a))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s-(%s)}}{2(%s)}$<br><br>'%(b,b*b,a*c*4,a))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s}}{2(%s)}$<br><br>'%(b,discriminant,a))
        a1('$x$ = $\\frac{-(%s)\pm %s}{2(%s)}$<br><br>'%(b,math.sqrt(discriminant),a))
        a1('$x$ = $\\frac{-(%s)}{2(%s)}$<br><br>'%(b,a))
        a1('$x$ = $%s$'%(root1))
        return ''.join(v),[str(root1)]
    elif(discriminant < 0):#condition for root < 0
        root1 = root2 = -b / (2 * a)
        imaginary = math.sqrt(-discriminant) / (2 * a)
        a1('Given Equation is ${}$<br><br>'.format(num1))
        a1('By converting the equation into $ax^2+bx+c=0$ by simplifyinng the equation <br><br>')
        a1('$=>{} = 0$<br><br>'.format(latex(s2)))
        a1('a = {} b = {} c = {}<br><br>'.format(a,b,c))
        a1('$x$ = $\\frac{-b\pm\sqrt{b^2-4ac}}{2a}$<br><br>')
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s^2-4(%s)(%s)}}{2(%s)}$<br><br>'%(b,b,a,c,a))
        a1('Multiplyig {} with {}<br><br>'.format(a,c))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s^2-4(%s)}}{2(%s)}$<br><br>'%(b,b,a*c,a))
        a1('Multiplyig {} with 4 <br><br>'.format(a*c))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s^2-(%s)}}{2(%s)}$<br><br>'%(b,b,a*c*4,a))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s-(%s)}}{2(%s)}$<br><br>'%(b,b*b,a*c*4,a))
        a1('$x$ = $\\frac{-(%s)\pm\sqrt{%s}}{2(%s)}$<br><br>'%(b,discriminant,a))
        a1('$x$ = $%.2f+i%.2f$  or  $x$ = $%.2f-i%.2f$<br><br>'%(root1, imaginary, root2, imaginary))
        a1("Two Distinct Complex Roots Exists: root1 = $%.2f+i%.2f$ and root2 = $%.2f-i%.2f$" %(root1, imaginary, root2, imaginary))
        return ''.join(v),(str(root1)+'i'+str(imaginary), str(root2)+'i'+str(imaginary))
def factor_multiple_func(n):
    nx=n
    v=[]
    a=v.append
    s=factor(simplify(process_sympy(n)))
    if str(expand(simplify(process_sympy(n)))).replace(' ','')==str(s).replace(' ',''):
        n=n.replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','')
        return '<p>'+n+' has no factor.So It can not be factorized</p>',n
    else:
        try:
            n=[]
            nt=[]
            s1=s.args
            for i in s1:
                if ')**' in str(i):
                    sol=i.args 
                    n.append(str(sympify(str(sol[0]))))
                    n.append(str(sympify(str(sol[0]))))
                    nt.append(str(sympify(str(sol[0]))))
                    nt.append(str(sympify(str(sol[0]))))
                    continue
                n.append(str(sympify(str(i))))
                nt.append(str(sympify(str(i))))
            sing=[]
            for i in nt:
                if i[0]=='-' and '+' not in i and '-' not in i[1:]:
                    sing.append(i)
                    n.pop(n.index(i))
                elif '+' not in i and '-' not in i[1:]:
                    sing.append(i)
                    n.pop(n.index(i))
                elif len(i)==1:
                    sing.append(i)
                    n.pop(n.index(i))
            s1=n
            s1=['('+i+')' for i in s1]
            st=''.join(s1)
            a('<p>The given polynomial is ${}$</p>'.format(nx))
            a('<p>The polynomial can be written as ${}$</p>'.format(latex(simplify(process_sympy(nx)))))
            s2=[str(i) for i in s1]
            x=s2[0]
            y=s2[1]
            if len(s1)==2:
                if x.find('+') or x.find('-'):
                    t=sympify(x,evaluate=False).args
                    l=[]
                    for i in t:
                        l.append(str(i))
                l1=[]
                for i in l:
                    l1.append('('+i+')*('+y+')')
                x3='+'.join(l1)
                if y.find('+') or y.find('-'):
                    t1=sympify(y,evaluate=False).args
                    l1=[]
                    for i in t1:
                        l1.append(str(i))
                    l2=[]
                    for j in l1:
                        for k in l:
                            l2.append('('+k+')*('+j+')')
                x4='+'.join(l2)
                if len(sing)>0:
                    mult=1
                    for i in sing:
                        mult=simplify(mult*(process_sympy(i)))
                    a('<p>=$('+latex(mult)+')$$('+x4+')$</p>')
                    a('<p>=$('+latex(mult)+')$$(('+latex(sympify(x3))+')$</p>')
                    a('<p>=$'+latex(s)+'$</p>')
                else:
                    a('<p>=$'+x4+'$</p>')
                    a('<p>=$'+x3.replace('**','*').replace('*','')+'$</p>')
                    a('<p>=$'+latex(s)+'$</p>')
                return ''.join(v).replace('**','^').replace('*','').replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),latex(s).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','')
            else:
                s3=poly_multiplication_func(str(st))
                t1=[]
                t2=[]
                for i,j in s3[0]:
                    t1.append(i)
                    t2.append(j)
                t1=t1[::-1]
                t2=t2[::-1]
                t2[0]=t1[0]
                if len(sing)>0:
                    mult=1
                    for i in sing:
                        mult=simplify(mult*(process_sympy(i)))
                    a('<p>=$('+latex(mult)+')$'+s3[3]+'</p>')
                    for i,j in zip(t1,t2):
                        a('<p>=$('+latex(mult)+')$$'+j+'$</p>')
                        a('<p>=$('+latex(mult)+')$$'+i+'$</p>')
                    a('<p>=$('+latex(mult)+')${}$'.format(latex(s))+'</p>')
                else:
                    for i,j in zip(t1,t2):
                        a('<p>=$'+j+'$</p>')
                        a('<p>=$'+i+'$</p>')
                    a('<p>=${}$'.format(latex(s))+'</p>')
                return ''.join(v).replace('**','^').replace('*','').replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),latex(s).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','')
        except Exception as e:
            a('<p>After factoring polynomials we get $'+latex(s)+'$</p>')
            return ''.join(v).replace('**','^').replace('*','').replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{',''),latex(s).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','')
#factor over difference over square example x^2-4
def factor_diff_sqr_func(n):
    fact=list(factor(process_sympy(n)).args)
    fact1=list(factor(process_sympy(n)).args)#spliting the factors
    if str(fact[0])=='-1':# if got '-ve' at 1st position
        fact=fact[1:]
        for i in fact:
            if '-' in str(i):
                fact.pop(fact.index(i))
                fact.append(i)
    else:
        fact=fact[::-1]
        for i in fact:
            if '-' in str(i):
                fact.pop(fact.index(i))
                fact.append(i)
    v=[]
    a=v.append
    a('<p>When you learn to factor quadratics, there are three other formulas that they usually introduce at the same time. The first is the "difference of squares" formula.</p>')
    a('<p>Remember from your translation skills that a "difference" means a "subtraction". So a difference of squares is something that looks like x<sup>2</sup> – 4. That is because 4 = 2<sup>2</sup>, so we really have x<sup>2</sup> – 2<sup>2</sup>, which is a difference of squares.</p>')
    a('<p>To factor this in the same way as usual for factoring:</p>')
    a(poly_multiplication_func1('(a+b)(a-b)')[0])
    a('<p>So we got the formula of <b>a<sup>2</sup>-b<sup>2</sup> = (a+b)(a-b)</b></p>')
    li=[]
    li2=[]
    a('<p>The given Polynomial is ${}$</p>'.format(n))
    if str(fact1[0])=='-1':
        a('<p>The given Polynomial can be written as $({})$</p>'.format(n))
        for i in fact[:len(fact)-1]:
                k=i.args
                li.append('($'+latex(k[0])+'$+$'+latex(k[1])+'$)($'+latex(k[0])+'$-$'+latex(k[1])+'$)<br>')
                li2.append('($'+latex(k[0])+'$+$'+latex(k[1])+'$)')
        li2=li2[::-1]
        li=li[::-1]
        a('<p>=(-)'+li[0]+'</p>')
        for i in li2[1:len(li2)-1]:
            li2[li2.index(i)]=li2[li2.index(i)-1]+li2[li2.index(i)]
        gh=[]
        for i,j in zip(li2[:len(li2)-1],li[1:]):
            a('<p>=(-)'+i+j+'</p>')
            gh.append('(-)'+i+j)
    else:
        for i in fact[:len(fact)-1]:
                k=i.args
                if isinstance(k[0],Integer):
                    k=list(i.args)[::-1]
                else:
                    k=i.args
                li.append('($'+latex(k[0])+'$+$'+latex(k[1])+'$)($'+latex(k[0])+'$-$'+latex(k[1])+'$)<br>')
                li2.append('($'+latex(k[0])+'$+$'+latex(k[1])+'$)')
        a('<p>='+li[0]+'</p>')
        for i in li2[1:len(li2)-1]:
            li2[li2.index(i)]=li2[li2.index(i)-1]+li2[li2.index(i)]
        gh=[]
        try:
            for i,j in zip(li2[:len(li2)-1],li[1:]):
                a('<p>='+i+j+'</p>')
                gh.append(i+j)
        except:
            pass
        
    return ''.join(v).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}','').replace('+-','-').replace('+ -','-'),latex(factor(process_sympy(n))).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}','').replace('<br>','')
#difference of cube factoring
def fact_diff_cube_func(n):
    n=n.replace('(','').replace(')','')
    nz=n
    ns=process_sympy(n)
    n1=n.split('-')#splitting with '-'
    l=[]
    l1=[]
    v=[]
    a=v.append
    mult=poly_multiplication_func1('(a-b)(a^2+ab+b^2)')#multiply using polymul
    a('<p>If we multiply the below expression:</p>')
    a(mult[0].replace('<br>','<br><br>'))
    a('<p>So we got the formula of <b>a<sup>3</sup>-b<sup>3</sup>=(a-b)(a<sup>2</sup>+ab+b<sup>2</sup>)</b></p>')
    for i in n1:
        z=i.split('^')
        l.append(z[0])
        l1.append(eval(z[1]))
    k=gcd(l1)
    l2=[i//3 for i in l1]
    s=prime_factors(k)
    count=0
    for i in s:
        if i=='3':
            count=count+1
    la=[]
    la2=[]
    for i in range(count):#factoring over power 3
        if k%3==0:
            la.append('($'+l[0]+'^{'+str(l2[0])+'}$'+'-'+'$'+l[1]+'^{'+str(l2[1])+'}$)($'+l[0]+'^{'+str(l2[0]*2)+'}+'+l[0]+'^{'+str(l2[0])+'}'+l[1]+'^{'+str(l2[1])+'}+'+l[1]+'^{'+str(l2[0]*2)+'}$)')
            la2.append('($'+l[0]+'^{'+str(l2[0]*2)+'}+'+l[0]+'^{'+str(l2[0])+'}'+l[1]+'^{'+str(l2[1])+'}+'+l[1]+'^{'+str(l2[0]*2)+'}$)')
            l2[0]=l2[0]//3
            l2[1]=l2[1]//3
            k=k/3
    a('<p>The given Polynomial is ${}$</p>'.format(nz))
    a('<p>By applying <b>a<sup>3</sup>-b<sup>3</sup>=(a-b)(a<sup>2</sup>+ab+b<sup>2</sup>)</b></p>')
    a('<p>='+la[0]+'</p>')
    list1=[]
    if len(la)>1:
        k1=0
        for i,j in zip(la[1:],la2[:len(la2)-1]):
            a('<p>='+i+''.join(la2[:k1+1])+'</p>')
            list1.append('='+i+''.join(la2[:k1+1]))
            k1=k1+1
    else:
        list1.append(la[0])
    return ''.join(v),list1[-1]
#factoring over summation of cube i.e. a^3+b^3
def fact_sum_cube_func(n):
    n=n.replace('(','').replace(')','')
    n1=n.split('+')#splitting with '+'
    l=[]
    l1=[]
    v=[]
    a=v.append
    mult=poly_multiplication_func1('(a+b)(a^2-ab+b^2)')
    a('<p>If we multiply the below expression:</p>')
    a(mult[0].replace('<br>','<br><br>'))
    a('<p>So we got the formula of <b>a<sup>3</sup>+b<sup>3</sup>=(a+b)(a<sup>2</sup>-ab+b<sup>2</sup>)</b></p>')
    for i in n1:
        z=i.split('^')
        l.append(z[0])
        l1.append(eval(z[1]))
    k=gcd(l1)
    l2=[i//3 for i in l1]
    s=prime_factors(k)
    count=0
    for i in s:
        if i=='3':
            count=count+1
    la=[]
    la2=[]
    for i in range(count):#splitting over power of 3
        if k%3==0:
            la.append('($'+l[0]+'^{'+str(l2[0])+'}$'+'+'+'$'+l[1]+'^{'+str(l2[1])+'}$)($'+l[0]+'^{'+str(l2[0]*2)+'}-'+l[0]+'^{'+str(l2[0])+'}'+l[1]+'^{'+str(l2[1])+'}+'+l[1]+'^{'+str(l2[0]*2)+'}$)')
            la2.append('($'+l[0]+'^{'+str(l2[0]*2)+'}-'+l[0]+'^{'+str(l2[0])+'}'+l[1]+'^{'+str(l2[1])+'}+'+l[1]+'^{'+str(l2[0]*2)+'}$)')
            l2[0]=l2[0]//3
            l2[1]=l2[1]//3
            k=k/3
    #a('The given Polynomial is ${}$<br><br>'.format(nz))
    a('<p>By applying <b>a<sup>3</sup>+b<sup>3</sup>=(a+b)(a<sup>2</sup>-ab+b<sup>2</sup>)</b></p>')
    a('<p>='+la[0]+'</p>')
    list1=[]
    if len(la)>1:
        k1=0
        for i,j in zip(la[1:],la2[:len(la2)-1]):
            a('<p>='+i+''.join(la2[:k1+1])+'</p>')
            list1.append('='+i+''.join(la2[:k1+1]))
            k1=k1+1
    else:
        list1.append(la[0])
    return ''.join(v),list1[-1]
#both addition and substraction of cube factorial
def sum_sub_cube(n):
    try:
        v=[]
        a=v.append
        n=n.replace('((','(').replace('))',')')
        z=process_sympy(n)
        if ')/(' in n:
            z1=n.split('/')
        else:
            z1=n.split(')(')
            z1[0]=z1[0]+')'
            z1[-1]='('+z1[-1]
            if len(z1)>2:
                for i in range(1,len(z1)-1):
                    z1[i]='('+z1[i]+')'
        for i in z1:    
            if ')(' in i:
                k=i.split(')(')
                k[0]=k[0]+')'
                k[-1]='('+k[-1]
                if len(k)>2:
                    for i in range(1,len(k)-1):
                        k[i]='('+k[i]+')'
                z1[z1.index(i)]=k[0]
                z1.append(k[-1])
                for i in k:
                    z1.append(i)
        for i in z1:    
            if ')(' in i:
                k=i.split(')(')
                k[0]=k[0]+')'
                k[1]='('+k[1]
                z1[z1.index(i)]=k[0]
                z1.append(k[1])
        a('<p>The given expression is ${}$</p>'.format(n))
        a('<p>By separating each expression we get</p>')
        z1=set(z1)
        z1=list(z1)
        for i in z1:
            a('<p>$'+i+'$</p>')
        for i in z1:
            if '-' in str(i)[1:]:
                try:
                    z=fact_diff_cube_func(i)
                    a(z[0]+'<br><br>')
                except:
                    z=factor_multiple_func(i)
                    a(z[0]+'<br><br>')
            else:
                try:
                    z=fact_sum_cube_func(i)
                    a(z[0]+'<br><br>')
                except:
                    z=factor_multiple_func(i)
                    a(z[0]+'<br><br>')
        a('<p>After getting indivisual factoring we can cancelout similar terms and The final result will be ${}$</p>'.format(latex(factor(process_sympy(n)))))
    except Exception as e:
        if '-' in str(n)[1:]:
            try:
                z=fact_diff_cube_func(n)
                a(z[0]+'<br><br>')
            except:
                z=factor_multiple_func(n)
                a(z[0]+'<br><br>')
        else:
            try:
                z=fact_sum_cube_func(n)
                a(z[0]+'<br><br>')
            except:
                z=factor_multiple_func(n)
                a(z[0]+'<br><br>')
        a('<p>After getting indivisual factoring we can cancelout similar terms and The final result will be ${}$</p>'.format(latex(factor(process_sympy(n)))))
    return ''.join(v).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}','').replace('+-','-').replace('+ -','-'),latex(factor(process_sympy(n))).replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}','').replace('+-','-')
#factoring trinomials 
def fact_trinomials_func(n):
    v=[]
    a=v.append
    a('The given expression is ${}$<br><br>'.format(n))
    a('By spliting expression into indivisual polynomials <br><br>')
    try:
        n=n.replace('((','(').replace('))',')')
        z=process_sympy(n)
        if ')/(' in n:
            z1=n.split('/')
        else:
            z1=n.split(')(')
            z1[0]=z1[0]+')'
            z1[-1]='('+z1[-1]
            if len(z1)>2:
                for i in range(1,len(z1)-1):
                    z1[i]='('+z1[i]+')'
        for i in z1:    
            if ')(' in i:
                k=i.split(')(')
                k[0]=k[0]+')'
                k[-1]='('+k[-1]
                if len(k)>2:
                    for i in range(1,len(k)-1):
                        k[i]='('+k[i]+')'
                z1[z1.index(i)]=k[0]
                z1.append(k[-1])
                for i in k:
                    z1.append(i)
        for i in z1:
            z=factor_multiple_func(i)
            a(z[0]+'<br><br>')
    except Exception as e:
        try:
            z=factor_multiple_func(n)
            a(z[0]+'<br><br>')
        except:
            z=sum_sub_cube(n)
            a(z[0]+'<br><br>')
    a('The final answer after symplifying all factors we get ${}$ '.format(latex(factor(process_sympy(n)))))
    return ''.join(v),'s'
#finding root of polynomials 
def poly_root_func(n):
    v=[]
    a=v.append
    try:
        s=factor_multiple_func(n)
        a(s[0])
        if 'So It can not be factorized' in s[0]:
            eval('sa')
        s1=LM(LM(process_sympy(n)))
        soln= latex(sympy.solve(sympify(process_sympy(n)),s1))
        a('<p>By factoring the polyomial as below</p>')
        a('<p>Polynomial Roots Calculator is a set of methods aimed at finding values of  x  for which   F(x)=0  </p>')
        a('<p>Rational Roots Test is one of the above mentioned tools. It would only find Rational Roots that is numbers  x  which can be expressed as the quotient of two integers</p>')
        a('<p>By factoring polynomial we get ${}$</p>'.format(latex(factor(process_sympy(n)))))
        sk=list(factor(process_sympy(n)).args)#splitting over factoring 
        sk=[str(i) for i in sk]
        sk1=[str(i) for i in sk]
        for i in sk:
            if '+' in i or '-'in i[1:]:
                pass
            else:
                sk1.remove(i)
        a('<p>After spliting the factors into indivisual expression</p>')
        l1=[]
        l2=[]
        for i in sk1:
            a('<p>$'+latex(sympify(i))+'= 0$</p>')
            l2.append('$'+latex(sympify(i))+'= 0$')
            l1.append(sympy.solve(sympify(i)))
            print(len(i))
        a('<p>By making each equation set to "0" we have calculate values of x</p>' )
        for i,j in zip(l2,l1):#root calculator
            a('<p>'+i+' has root i.e $'+latex(j)+'$</p>')
        return ''.join(v).replace('$$$$</p>','').replace('\\times','*').replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}','').replace('+-','-').replace('+ -','-').replace('\\left','').replace('\\right',''),str(l1)[1:-1]
    except:
        s=factor(process_sympy(n))
        a('<p>${}$ can not be factorized </p>'.format(n))
        a('<p>It simplify as ${}$</p>'.format(latex(s)))
        a('<p>Making equation ${}$ = 0</p>'.format(n))
        a('<p>Finding the root by making f(x)=0 </p>')
        a('<p>We get root of the equation is ${}$'.format(latex(sympy.solve(s))))
        return ''.join(v).replace('\\times','*').replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}','').replace('+-','-').replace('+ -','-').replace('\\left','').replace('\\right','').replace('\\',''),latex(sympy.solve(s)).replace('\\times','*').replace('$','').replace('\\left(','(').replace('\\right)',')').replace('\\frac{','').replace('}{','/').replace('}','').replace('{','').replace('\\times{}','').replace('+-','-').replace('+ -','-').replace('\\left','').replace('\\right','').replace('\\','')
def poly_remainder_func(num1,num2):
    input2=process_sympy(num2)
    y=sympy.solve(input2)
    v=[]
    a=v.append
    import re
    z1= re.findall("[a-zA-Z]", num1)
    z1=list(set(z1))
    if len(z1)>1:
        return redirect('/polynomials/remainder-theorem-calculator/')
    z = re.findall("[a-zA-Z]", str(simplify(input2)))
    z=list(set(z))
    if len(z)>1 and len(y)!=1:
        return redirect('/polynomials/remainder-theorem-calculator/')
    a('<p>Given values are </p>')
    a('<p>f({}) = {}</p>'.format(z[0],num1))
    a('<p>{} = {}.</p>'.format(z[0],y[0]))
    b=poly_Evaluation_func(num1+',x='+str(y[0]))
    a(b[0])
    a('<p>The remainder of given polynomial is {}.</p>'.format(b[1]))
    return ''.join(v),b[1]
