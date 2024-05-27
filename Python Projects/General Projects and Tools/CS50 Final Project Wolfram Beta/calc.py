import numpy as np
import math as mt
import seaborn as sns
import pandas as pd




xo=0
xf=500

def calc(func='x^3-8*x-48',xo=xo,xf=xf,solved=True,acc=0.001):
    # return('hello')
    # print(f'calc, {acc}')
    func0=func.replace('x','xo')
    func0=func0.replace('exop','exp')
    try:
        sol0=eval(func0)
    except:
        return 0,False
    # print(f'calc from {xo} to {xf}')
    
    funcf=func.replace('x','xf')
    funcf=funcf.replace('exfp','exp')
    try:
        solf=eval(funcf)
    except:
        return 0,False
    
    if abs(solf)<acc:

        return xf,True
    if sol0*solf<=0:
        # root in between
        # print('sol in between')
        xm=(xf+xo)/2
        funcm=func.replace('x','xm')
        funcm=funcm.replace('exmp','exp')
        try:
            solm=eval(funcm)
        except:
            return 0,False
        try:
            res=sol0*solm
            if abs(res)>100_000_000:
                print('error 3 approaching infinity')
                return 0,False
        except:
            print('error 4')
            return 0,False
        
        if res<=0:
            # root in between
            xf,solved=calc(func,xo=xo,xf=xm,solved=solved,acc=acc)
        else:
            xf,solved=calc(func,xo=xm,xf=xf,solved=solved,acc=acc)
    else:

        return 0,False
    return xf,True
def SOLVE_working(func='x^3-2*x^2+3',custr=[]):
    
    rules=pd.read_csv('mathrules.csv')
    for id,r in rules.iterrows():
        func=func.replace(r['in'],r['out'])
    # print('ed_func',func)
    if len(custr)==2:
        xm=(custr[0]+custr[1])/2+0.5
        x1,solved1=calc(func,xo=xm,xf=custr[1])
        x2,solved2=calc(func,xo=xm,xf=custr[0])
    else:
        x1,solved1=calc(func,xo,xf)
        x2,solved2=calc(func,xo,-xf)
    
    if solved1 and solved2:
        L=x1-x2
        
        range=[x2-L/10,x1+L/10]
        # print(x1,x2)
        sol=f'At least 2 roots were found @ x={x1:0.2f},{x2:0.2f}.'
        num=50
    if solved1 and not solved2:
        sol=f'At least 1 root was found @ x={x1:0.2f}.'
        range=[-5,x1+5]
        num=50
        # print(x1)
    if solved2 and not solved1:
        num=50
        sol=f'At least 1 root was found @ x={x2:0.2f}.'
        range=[x2-5,5]
        # print(x2)
    # else:
    if not solved1 and not solved2:
        num=500
        sol=f'In the region studied, no clear root was found!'
        range=[-5,5]
    if abs(x1)>100 or abs(x2)>100:
        num=500
    print(sol)
    if len(custr)==2:
        range=custr
    x=np.linspace(start=range[0],stop=range[1],num=num)
    try:
        print(func,'should be used')
        y=eval(func)
        print(func,'used')
    except:
        y=x*0
        print(0,'used')
    return x,y,sol

# endregion


def SOLVE(func='x^3-2*x^2+3',custr=[],acc=0.001):
    print(f'solve, {acc}')
    rules=pd.read_csv('mathrules.csv')
    for id,r in rules.iterrows():
        func=func.replace(r['in'],r['out'])
        # print(r['in'],'ed_func',func)

    print('ed_func',func)
    
    if len(custr)==2:
        xm=(custr[0]+custr[1])/2+0.5
        x1,solved1=calc(func,xo=xm,xf=custr[1],acc=acc)
        x2,solved2=calc(func,xo=xm,xf=custr[0],acc=acc)
    else:
        x1,solved1=calc(func,xo,xf,acc=acc)
        x2,solved2=calc(func,xo,-xf,acc=acc)
    

    if solved1 and solved2:
        L=x1-x2
        
        range=[x2-L/10,x1+L/10]
        # print(x1,x2)
        sol=f'👌 At least 2 roots were found @ x={x1:0.2f},{x2:0.2f}.'
        num=50
        nosol=False
    if solved1 and not solved2:
        sol=f'👌 At least 1 root was found @ x={x1:0.2f}.'
        range=[-5,x1+5]
        num=50
        nosol=False
        # print(x1)
    if solved2 and not solved1:
        num=50
        sol=f'👌 At least 1 root was found @ x={x2:0.2f}.'
        range=[x2-5,5]
        nosol=False
        # print(x2)
    # else:
    if not solved1 and not solved2:
        num=500
        nosol=True
        sol=f'🙁 In the region studied, no clear root was found!'
        range=[-5,5]
    if abs(x1)>100 or abs(x2)>100:
        num=500
    print(sol)
    if len(custr)==2:
        range=custr
    x=np.linspace(start=range[0],stop=range[1],num=num)
    try:
    # print(func,'should be used')
        y=eval(func)
        # print(f'{y}')
        if nosol or abs(x1-x2)<1:
            # print(f'y')
            # find root in between
            print('## no bisection root')
            y_min=abs(y).min()
            if y_min<0.01:
                print('## solved using basic graphing')
                x_mins=x[np.where(y==y_min)[0]]
            
                xm=(x_mins).mean()

                func_star=func.replace('x','xm')
                func_star=func_star.replace('exmp','exp')
                y_star=eval(func_star)

                if y_star<=y_min:
                    # sol=xm
                    sol=f'🙂 At least 1 root was found @ x≈{xm:0.2f}.'
                else:
                    sol=f'🙂 At least 1 root was found @ x≈{x_mins[0]:0.2f}.'
                        # sol=x_mins[0]
            else:
                print('ok so no min and no bisec we will try graph')
                y1=np.insert(y,0,0)
                y2=np.append(y,0)
                try:
                    comb=np.sign(y1*y2)
                    print('here??')
                    sols=[]
                    for i in np.where(comb==-1)[0]:
                        print(f'xo={x[i-1]},xf={x[i+1]},func={func}')
                        s=calc(xo=x[i-1],xf=x[i+1],func=func,acc=0.001)
                        print(f's={s}')
                        print(f'root should be {s[0]:0.2f}')
                        sols.append(s[0])
                    if len(sols)==1:
                        sol=f'😅 At least 1 root was found @ x≈{sols[0]:0.2f}.'
                    elif len(sols)==2:
                        sol=f'😅 At least 2 roots were found @ x≈{sols[0]:0.2f},x≈{sols[1]:0.2f} .'
                except:
                    y=x*0             
    # print(func,'used')
    except:
        y=x*0
        print(0,'used')
    if (np.isnan(y).sum()>0 or np.isinf(y).sum()>0):
        y=x*0
        sol='❌ Function Can not be graphed for the selected range (might contain a nan / devision by 0)'
    return x,y,sol
x=12
eval('print(mt.sin(x))')