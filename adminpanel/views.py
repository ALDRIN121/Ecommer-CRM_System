from django.contrib import messages
from django.shortcuts import render,redirect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import static.images as img 
import io
import urllib, base64
from home.models import Add_info, Prdlist, Review, Transact
import smtplib, ssl
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import Extract
from collections import Counter
from django.db.models import F

# Create your views here.

# - Change the title name ----DONE
# - Add location wise demography ---- DONE
# - Add products page ---- DONE
# - Add view all users ---- DONE


def mainpg(request):
    
    a4_dims = (5.0, 5.0)
    df = pd.read_csv('file1.csv')
    fig,ax = plt.subplots(figsize=a4_dims)
    labels = 'male','female'
    explode = (0, 0.05)
    plt.pie(df['sex'].value_counts(), labels=labels, explode=explode, autopct='%1.0f%%')
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)


    details = df.apply(lambda x : True
            if x['products'] == "Laptop" else False, axis = 1) 
    num_rows = len(df[details == True].index)
    
 

    details1 = df.apply(lambda x : True
            if x['products'] == "Speaker" else False, axis = 1) 
    num_rows1 = len(df[details1 == True].index)


    details2 = df.apply(lambda x : True
            if x['products'] == "TV" else False, axis = 1) 
    num_rows2 = len(df[details2 == True].index)

    details3 = df.apply(lambda x : True
            if x['products'] == "Mobile" else False, axis = 1) 
    num_rows3 = len(df[details3 == True].index)



    rar = countplt()
    img2= ageplt() 

    pop = df.sex.mode()
    s = df['location'].value_counts() 
    lowloc = s.index[-1]
    highloc =s.index[0]

    prod = df.sex.mode()
    
    f = df['products'].value_counts() 
    lowprod = f.index[-1]
    highprod =f.index[0]

    totprod =df['products'].count()


    c = Review.objects.count()

    
    return render(request,'dashboard.html',{'image':rar,'image1':uri,'population':pop[0],'lowloc':lowloc,'highloc':highloc,'highprod':highprod,'lowprod':lowprod,'laptop':num_rows,'speaker':num_rows1,'shirt':num_rows2,'mobile':num_rows3,'totprod':totprod,'image2':img2,'count': c})


def countplt():
    a4_dims = (7.0, 5.0)
    df = pd.read_csv('file1.csv')
    fig,ax = plt.subplots(figsize=a4_dims)
    sns.countplot(x="location", data=df)
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri1 =  urllib.parse.quote(string)
    return uri1

    
    
def ageplt():
    a4_dims = (7.0, 5.0)
    df = pd.read_csv('file1.csv')
    fig,ax = plt.subplots()
    df.groupby('sex').age.plot(kind='kde')
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri2 =  urllib.parse.quote(string)
    return uri2


def reviewpg(request):


        review = Review.objects.filter(enquired=False)

        return render(request,'reviewadmin.html',{'review':review})


def emailpg(request):
        if request.method == 'POST':
                btn = request.POST['btn1']
                ids = request.POST['id']

        em = User.objects.get(username=btn).email
        print(em)


        
        


        return render (request,'sent_email.html',{'email':em,'id':ids})





def sent_email(request):

        if request.method == 'POST':
                msg = request.POST['msg']
                email=request.POST['email']
                ids= request.POST['id']



        prompt_msg = msg
        file = open("datas.txt")
        data = file.readlines()
        print(data[1])

        file.close()
        user = data[0]
        password = data[1]

        sender = email

        subject = "Enquiry about your feedback "
        message = "Subject: {} \n\n{}".format(subject, prompt_msg)
        send_to = ("{}".format(sender))

        mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        mail.ehlo()
        mail.login(user, password)
        mail.sendmail(user, send_to, message)
        mail.close()
        print("Success Email!")

        Review.objects.filter(id=ids).update(enquired=True)

        return redirect('/adminpanel/review')


def demographic(request):

        return render(request,"documets.html")

def loc_prd(request):
        df = pd.read_csv('file1.csv')

        if request.method == 'POST':
                loc = request.POST['btn']

                male=len(df[(df['location'] == loc) & (df['sex'] == 'male')])
                female=len(df[(df['location'] == loc) & (df['sex'] == 'female')])
                a4_dims = (5.0, 3.0)
                fig,ax = plt.subplots(figsize=a4_dims)
                labels = 'male','female'
                explode = (0, 0.05)
                plt.pie([male,female], labels=labels, explode=explode, autopct='%1.0f%%')
                #convert graph into dtring buffer and then we convert 64 bit code into image
                buf = io.BytesIO()
                fig.savefig(buf,format='png')
                buf.seek(0)
                string = base64.b64encode(buf.read())
                uri =  urllib.parse.quote(string)
                print(loc)



        return render(request,'documets.html',{
                'pie': uri,
                'line':loc_ageplt(loc),
                'count':loc_countplt(loc),
                'lineplt':loc_lineplt(loc),
                'mob':mobile_pie(loc),
                'lap':lap_pie(loc),
                'speaker':speaker_pie(loc),
                'tv':tv_pie(loc),
                })
        

def loc_ageplt(x):
    a4_dims = (5.0, 3.0)
    df = pd.read_csv('file1.csv')
    fig,ax = plt.subplots()
    df[df['location']==x].age.plot(kind='kde')
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri2 =  urllib.parse.quote(string)
    return uri2



def loc_countplt(x):

        a4_dims = (5.0, 3.0)
        df = pd.read_csv('file1.csv')
        fig,ax = plt.subplots(figsize=a4_dims)
        sns.countplot(x=df.products[df.location ==x],data=df)
        #convert graph into dtring buffer and then we convert 64 bit code into image
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri1 =  urllib.parse.quote(string)
        return uri1




def loc_lineplt(x):

        a4_dims = (7.0, 5.0)
        df = pd.read_csv('file1.csv')
        fig,ax = plt.subplots(figsize=a4_dims)
        p=df.products[df.location ==x]
        a=df.age[df.location ==x]
        s=df.sex[df.location ==x]
        sns.lineplot(x=p,y=a,hue=s,data=df)
        #convert graph into dtring buffer and then we convert 64 bit code into image
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri1 =  urllib.parse.quote(string)
        return uri1

def mobile_pie(x):


        a4_dims = (5.0, 5.0)
        df = pd.read_csv('file1.csv')
        fig,ax = plt.subplots(figsize=a4_dims)
        labels = "samsung","oppo","xiomi","apple"
        explode = (0.03, 0.03,0.03,0.03)
        
        gaga=df.Brand[(df.products =='Mobile')& (df.location==x)]
        plt.pie(gaga.value_counts(), labels=labels, autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
        #convert graph into dtring buffer and then we convert 64 bit code into image
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri =  urllib.parse.quote(string)


        return uri


def lap_pie(x):


        a4_dims = (5.0, 5.0)
        df = pd.read_csv('file1.csv')
        fig,ax = plt.subplots(figsize=a4_dims)
        labels = "asus","hp","dell","lenovo"
        explode = (0.03, 0.03,0.03,0.03)
        gaga=df.Brand[(df.products =='Laptop')& (df.location==x)]
        plt.pie(gaga.value_counts(), labels=labels, explode=explode, autopct='%1.0f%%')
        #convert graph into dtring buffer and then we convert 64 bit code into image
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri =  urllib.parse.quote(string)


        return uri


def speaker_pie(x):


        a4_dims = (5.0, 5.0)
        df = pd.read_csv('file1.csv')
        fig,ax = plt.subplots(figsize=a4_dims)
        names = ["jbl","sony","bose","harman"]
        labels = list(names)
        explode = (0.03, 0.03,0.03,0.03)
        gaga=df.Brand[(df.products =='Speaker')& (df.location==x)]
        plt.pie(gaga.value_counts(), labels=labels, explode=explode, autopct='%1.0f%%')
        #convert graph into dtring buffer and then we convert 64 bit code into image
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri =  urllib.parse.quote(string)


        return uri

def tv_pie(x):


        a4_dims = (5.0, 5.0)
        df = pd.read_csv('/file1.csv')
        fig,ax = plt.subplots(figsize=a4_dims)
        labels = "LG","VU","sony","Toshiba"
        explode = (0.03, 0.03,0.03,0.03)
        gaga=df.Brand[(df.products =='TV')& (df.location==x)]
        plt.pie(gaga.value_counts(), labels=labels, explode=explode, autopct='%1.0f%%')
        #convert graph into dtring buffer and then we convert 64 bit code into image
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri =  urllib.parse.quote(string)


        return uri



def add_prd(request):






        return render(request,'add_prd.html')

def addpd(request):
        try:


                if request.method == 'POST':
                        prdcat = request.POST['prdcat']
                        brnd = request.POST['brnd']
                        prdname = request.POST['prdname']
                        prddetails = request.POST['prddetails']
                        prdprice = request.POST['prdprice']
                        stock = request.POST['stock']

                        prdimg = request.FILES['prdimage']

                        prd = Prdlist(
                                product = prdcat,
                                brand=brnd,
                                brand_pd=prdname,
                                pd_details=prddetails,
                                price=prdprice,
                                img=prdimg,
                                stock=stock
                        )

                        prd.save()

                        return redirect('/adminpanel')

        except Exception as e:
                messages.info(request, "Product Already Exists")

                return redirect('/adminpanel/add_prd')
                



def allusr(request):
        data = Add_info.objects.all()
        return render(request,'alluser.html',{'data':data})

def allorder(request):
        data = Transact.objects.all()
        return render(request,'allorder.html',{'data':data})

def monthly(request):

        return render(request,'monthly.html')

def monthlys(request):
        if request.method == 'POST':
                month=request.POST['month']
        months = Transact.objects.annotate(month_stamp=Extract('date', 'month')).filter(month_stamp=month).all()
        print(months)
        return render(request,'monthly.html',{'data': months})

def alerts(request):
        d=Review.objects.filter(review_analysis="Negative").values("brand_pd","username")
        s=d.annotate(mc=Count('brand_pd')).order_by('-mc')[0]
        print(s)
        d1=Review.objects.filter(review_analysis="Positive").values("brand_pd","username")
        s1=d1.annotate(mc=Count('brand_pd')).order_by('-mc')[0]
        return render(request,'alerts.html',{
                'data': s,
                'data1': s1
                })
def stocks(request):
        data = Prdlist.objects.all()
        return render(request,'stocks.html',{'data':data})
        
def add_stocks(request):
        if request.method == 'POST':
                v_id= request.POST['id']
                stoc = request.POST['stocks']
                Prdlist.objects.filter(id=v_id).update(stock=F('stock')+ stoc)
                print("hello")
        return redirect('/adminpanel/stocks')
        
def view_stock(request):
        data = Prdlist.objects.all()
        return render(request,'viewstocks.html',{'data':data})