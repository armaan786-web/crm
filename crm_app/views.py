from django.shortcuts import render,redirect
from django.urls import reverse
from django.conf import settings
from crm_app.EmailBackEnd import EmailBackEnd
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProductForm,UpiForm,KycForm
from django.views import View
from .models import *
from django.contrib.auth import get_user_model
# Create your views here.



def Error404(request, exception):
    return render(request,'errors/404.html')

@login_required(login_url='login')
def home(request):
    product = Prodcut.objects.all()
    return render(request,"homepage/home.html",{'product':product})
    
@login_required(login_url='login')
def user_dashboard(request):
    product = Prodcut.objects.all()
    upi_gateway = upi.objects.all()

    if request.method == "POST":
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        upi_id = request.POST.get('upi_id')
        reference_number = request.POST.get('reference_number')
        print("amount",amount,"method",payment_method,"upi_id",upi_id,"refernce",reference_number)

        prof = Profile.objects.get(user = request.user)
        upi_number = upi.objects.get(upi_number =upi_id)
        rec = recharge.objects.create(user=prof,recharge_amount=amount,upi=upi_number,reference_number=reference_number)
        rec.save()



    if request.user.is_authenticated:
        user = request.user
        print(user)
        rec = recharge.objects.filter(user__user=user)
        total_amount = 0
        # recharge_product = [p for p in recharge.objects.all() if p.user==user]
        recharge_product = recharge.objects.all()
 
 
        totalrecharge = len(recharge.objects.filter(user__user=request.user))
        print("total recharge",recharge_product)
        if recharge_product:
            for p in recharge_product:
                total_amount += p.recharge_amount
                print("total",total_amount)
            return render(request,"user/user_dashboard.html",{'product':product,'upi_gateway':upi_gateway,'total_amount':total_amount})
               
    
    return render(request,"user/user_dashboard.html",{'product':product,'upi_gateway':upi_gateway})

def admin_login(request):
    if request.method == "POST":
        user=EmailBackEnd.authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        
        if user!=None:
            login(request,user)
            if request.user.is_superuser == 1:
                return HttpResponseRedirect('/')
            else:
                return redirect('user_dashboard')
            # elif user.user_type=="2":
            #     return HttpResponseRedirect(reverse("staff_home"))
            # else:
            #     return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request,"Invalid Login Or Password !!")
            return redirect('login')
            # return HttpResponseRedirect("login")
    # if request.user.is_superuser == 1:
    #     return redirect('home')
    else:
        return render(request,"homepage/login.html")


    # return render(request,"homepage/login.html")

def signup(request):

    if request.method == "POST":
        reference_no = request.POST.get("reference_no")
        username = request.POST.get("username")
        mobile = request.POST.get("mob_no")
        password = request.POST.get("password")
        
        try:
            user = User.objects.create_user(username=username,password=password)
            user.profile.mobile = mobile  
            user.save()
            messages.success(request,"Registration sucessfully......")
            return redirect("login")
        except:
            messages.error(request,"somthing wrong try again!!")
            return redirect("signup")
    return render(request,"homepage/register.html")


def profile(request):
    return render(request,"homepage/profile.html")


def user_list(request):
    # User = get_user_model()
    # users = User.objects.all()
    profile = Profile.objects.all()
    return render(request,"customer/user_list.html",{'profile':profile})


class add_product(View):

    def get(self,request):
        form = ProductForm()
        return render(request,'Products/add_product.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form2 = ProductForm
        form = ProductForm(data=request.POST,files=request.FILES)
        
        
        if form.is_valid():

            name = form.cleaned_data['name']
            if Prodcut.objects.filter(name = name).exists():
                messages.warning(request,name + " is already Taken ")
                return redirect('add_product')
            form.save()
            messages.success(request,'Product!! Added')
        # return HttpResponseRedirect("Products/add_product.html",{'form':form})
        return render(request,"Products/add_product.html",{'form':form2})

class add_kyc(View):

    def get(self,request):
        form = KycForm()
        return render(request,'kyc/add_kyc.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        # form2 = ProductForm
        form = KycForm(data=request.POST)
        
        
        if form.is_valid():
            usr = request.user
            holder_name = form.cleaned_data['holder_name']
            account_number = form.cleaned_data['account_number']
            bank_name = form.cleaned_data['bank_name']
            branch = form.cleaned_data['branch']
            ifsc_code = form.cleaned_data['ifsc_code']
            Kyc = kyc(user=usr,holder_name=holder_name,account_number=account_number,bank_name=bank_name,branch=branch,ifsc_code=ifsc_code)
            Kyc.save()
            messages.success(request,'Congratulations!! Profile Updated Successfully') 
            return redirect('kyc')
            # form.save()
            # messages.success(request,'Product!! Added')
        # return HttpResponseRedirect("Products/add_product.html",{'form':form})
        # return render(request,"kyc/add_kyc.html",{'form':form2})
def kyc_list(request):
    
    Kyc = kyc.objects.filter(user=request.user)
    print(Kyc)
    return render(request,"kyc/kyc_list.html",{'kyc':Kyc})

def admin_kyc_list(request):
    
    
    Kyc = kyc.objects.all()
   
    return render(request,"admin_kyc/kyc_list.html",{'kyc':Kyc})


def product_list(request):
    product = Prodcut.objects.all()
    return render(request,"Products/product-list.html",{'product':product})



def product_delete(request,pk):
    queryset = Prodcut.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, ' Deleted Successfully')
        return redirect('/product_list')
    return render(request, 'Products/product-list.html')


def recharge_request(request):
    Recharge = recharge.objects.all()
    return render(request,"Accounts/recharge_request.html",{'Recharge':Recharge})



def recharge_status(request,id):
    Recharge=recharge.objects.get(id=id)
    Recharge.status= "accept"
    Recharge.save()
    return redirect('recharge_request')

def recharge_rejected(request,id):
    Recharge=recharge.objects.get(id=id)
    Recharge.status= "rejected"
    Recharge.save()
    return redirect('recharge_request')

def recharge_list(request):
    Recharge = recharge.objects.all()
    return render(request,"recharge/recharge_list.html",{'Recharge':Recharge})
def withdraw_request(request):
    return render(request,"Accounts/withdraw_request.html")

class add_upi(View):

    def get(self,request):
        form = UpiForm()
        return render(request,'upi/add_upi.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        # form2 = ProductForm
        form = UpiForm(request.POST)
        
        
        if form.is_valid():

            upi_name = form.cleaned_data['select_upi']
            if upi.objects.filter(select_upi = upi_name).exists():
                messages.warning(request,upi_name + " is already Taken ")
                return redirect('add_upi')
            form.save()
            messages.success(request,'Product!! Added')
            return redirect('add_upi')
        # return HttpResponseRedirect("Products/add_product.html",{'form':form})
        # return render(request,"Products/add_product.html",{'form':form2})

def upi_list(request):
    upi_list = upi.objects.all()
    return render(request,'upi/upi-list.html',{'upi_list':upi_list})

def booking(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Prodcut.objects.get(id=product_id)
    booking=Booking(user=user,product=product)
    booking.save()

def booking_list(request):
    booking = Booking.objects.filter(user=request.user)   
    return render(request,'booking/booking_list.html',{'booking':booking})

def admin_booking_list(request):
    booking = Booking.objects.all()
    return render(request,'admin_booking/booking_list.html',{'booking':booking})