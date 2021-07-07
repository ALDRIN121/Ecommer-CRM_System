from django.contrib.messages.api import add_message
from django.shortcuts import render,redirect
from .models import Prdlist,Add_info,Transact,Review,Cart
from django.contrib.auth.models import User,auth
from django.contrib import messages
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from django.db.models import Sum
from django.contrib.auth import logout

# Create your views here.

# - Create Qnt in db and add when selected to product list ---- DONE
# - Show reviews for each project under ---- DONE
# - Add cart:
#    -> Need to create design page for cart got to cart page etc ---- DONE
#    -> Show all values to cart and give total ---- DONE
#    -> Add to cart option ---- DONE
#    -> Create Db for cart ---- DONE
#    -> Db save cart data wit total ----DONE
#    -> Edit cart 
#             -> Create page for edit ---- DONE
#             -> Show current value in cart and edit accordingly ---- DONE
#             -> Problem of th the data cannot be taken in with a single edit button --- DONE
#                so need to assign edit button for each with respective id
#    -> After checkout save to transaction table ---- DONE
# - Add payment PAYTM
# - Add Return Policy
# - Show the account icon and check icons  ---- DONE
# - Logout button ---- DONE
# - if usrname already exits then show msg ---- DONE
# - Change watch pic in home page ---- DONE
# - Change title ---- DONE
# - Add price in transact ---- DONE
# - Fix the speaker not showing ---- DONE


def mainpg(request):

    mobile = Prdlist.objects.filter(product='mobile').last()
    laptop = Prdlist.objects.filter(product='Laptop').last()
    tv = Prdlist.objects.filter(product='TV').last()
    speaker = Prdlist.objects.filter(product='Speaker').last()

    uname = request.user.username

    review = Transact.objects.filter(username=uname).filter(review_given=False)

    latest = Prdlist.objects.last()


    

    

    




    return render(request,'index.html',{'v' : mobile,'v1': laptop,'v2': tv ,'v3': speaker,'reviews' : review,'latest':latest})


def mobile(request):
    mobile = Prdlist.objects.filter(product='mobile')

    return render(request,'shop.html',{'val': mobile,'title': 'Mobile'})

def laptop(request):
    val = Prdlist.objects.filter(product='Laptop')

    return render(request,'shop.html',{'val': val,'title': 'Laptop'})

def tv(request):
    val = Prdlist.objects.filter(product='TV')

    return render(request,'shop.html',{'val': val,'title': 'TV'})


def speaker(request):
    val = Prdlist.objects.filter(product='Speaker')

    return render(request,'shop.html',{'val': val,'title': 'Speaker'})


def product_detail(request):

    if request.method == 'POST':
        prd = request.POST['btn1']
    val = Prdlist.objects.filter(brand_pd=prd)
    review = Review.objects.filter(brand_pd=prd).order_by('-id')[:3]

    return render(request,'product_details.html',{'val': val,'review':review})

def login(request):

    return render(request,'login.html')


def register(request):



    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        pswd1 = request.POST['pass']
        gender = request.POST['gender']
        age = request.POST['age']
        location = request.POST['location']

        if User.objects.filter(username = uname).first():
            messages.error(request, "This username is already taken")
            return redirect("/signup")
        else:
            user = User.objects.create_user(username = uname, password = pswd1, email = email, first_name=fname,last_name=lname)
            add_info = Add_info(
                username=uname,
                gender=gender,
                age=age,
                location=location
            )

            user.save()
            add_info.save()
            print("DONE")
            return redirect('/')




def signup(request):
    return render(request,'register.html')

def signin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pswd1 = request.POST['pass']

        user = auth.authenticate(username = uname, password = pswd1)

        if user is not None:
            auth.login(request,user)
            return redirect('/home')
            
        else:
            messages.info(request,'wrong credentials')
            return redirect('/')


def transact(request):
    if request.method == 'POST':
        qnt = request.POST['qnt']
        uname = request.user.username
        if 'btn1' in request.POST:
            pdname = request.POST['btn1']
            info = Add_info.objects.get(username=uname)
            # age = Add_info.objects.get(username=uname)
            # location = Add_info.objects.get(username=uname)
            product = Prdlist.objects.get(brand_pd=pdname)
            # brand = Prdlist.objects.get(brand_pd=pdname)
            print(qnt)
            price = product.price
            Total = int(qnt) * int(price)
            transt = Transact(
                username=uname,
                product=product.product,
                brand=product.brand,
                brand_pd=pdname,
                gender=info.gender,
                age=info.age,
                location=info.location,
                Quantity=qnt,
                Total_Price= str(Total)
            )

            transt.save()
            return redirect("/home")

        elif 'btn2' in request.POST:

            prd = request.POST['btn2']
            product = Prdlist.objects.get(brand_pd=prd)
            price = product.price
            Total = int(qnt) * int(price)

            add_to_cart = Cart(
                username=uname,
                product=product.product,
                brand=product.brand,
                brand_pd=prd,
                Quantity=qnt,
                Total_Price= Total,
                price=price
                
            )
            add_to_cart.save()
            return redirect("/home")




def review(request):
    if request.method == 'POST':
        ids = request.POST['btn1']
        print(ids)
    gg = Transact.objects.filter(id=ids).values('brand_pd').first()
    uname = request.user.username


    return render(request,'review.html',{'prd':gg,'name':uname,'ids':ids})
    



def review_save(request):
    if request.method == 'POST':
        rev = request.POST['review']
        ids = request.POST['id']

        prd = Transact.objects.filter(id=ids).first()

        uname = request.user.username


    


    snt = SentimentIntensityAnalyzer()

    sent_dict = snt.polarity_scores(rev)

    if sent_dict['compound'] >= 0.05:
        review_analysis = 'Positive'
		

    elif sent_dict['compound'] <= - 0.05 :
        review_analysis= 'Negative'
		

    else :
        review_analysis='Neutral'

		


    revi = Review(
        brand_pd=prd.brand_pd,
        username=uname,
        review=rev,
        review_analysis=review_analysis
    )

    revi.save()
    Transact.objects.filter(username=uname).filter(id=ids).update(review_given=True)
    
            
            
    
    

    return redirect("/home")


def cart(request):

    uname = request.user.username
    rev = Cart.objects.filter(username=uname).filter(sold=False)
    total_sum = Cart.objects.filter(username=uname).filter(sold=False).aggregate(Sum('Total_Price'))
    print(total_sum)



    return render(request,'cart.html',{'rev':rev,'total':total_sum})

def cart_checkout(request):

    uname = request.user.username
    checkout= Cart.objects.filter(username=uname)
    info = Add_info.objects.get(username=uname)
    transt = Transact(
    username=uname,
    product=checkout.product,
    brand=checkout.brand,
    brand_pd=checkout.pdname,
    gender=info.gender,
    age=info.age,
    location=info.location,
    Quantity=checkout.Quantity,
    Total_Price= checkout.Total_Price
    )
    transt.save()


def checkout(request):

    uname = request.user.username
    
    cart = Cart.objects.filter(username=uname)
    info = Add_info.objects.get(username=uname)




    for c in cart:

        transt = Transact(
        username=uname,
        product=c.product,
        brand=c.brand,
        brand_pd=c.brand_pd,
        gender=info.gender,
        age=info.age,
        location=info.location,
        Quantity=c.Quantity,
        Total_Price= c.Total_Price
        )
        transt.save()
        Cart.objects.filter(username=uname).update(sold=True)

    return redirect('/home')


def edit_cart(request):
    uname = request.user.username

    if request.method == 'POST':
        rev = request.POST['qnt']
        pid = request.POST['id']


        print(rev)
        print(pid)



        price = Cart.objects.filter(username=uname).filter(id=pid).first()
        print(price.price)
     

        total = int(price.price) * int(rev)
        Cart.objects.filter(username=uname).filter(id=pid).update(Quantity=rev,Total_Price=total)

    return redirect('/cart')

def update_cart(request):
    uname = request.user.username
    if request.method == 'POST':
        v_id = request.POST['btn']
    rev = Cart.objects.filter(username=uname).filter(sold=False).filter(id=v_id)

    print(v_id)
    return render(request,'edit_cart.html',{'rev':rev})


def logout_user(request):
    logout(request)
    return redirect("/")


        
