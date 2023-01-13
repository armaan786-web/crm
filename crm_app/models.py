from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .utils import generate_ref_code

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(to=User,on_delete=CASCADE)
    mobile = models.CharField(max_length=100)
    referral_id = models.CharField(max_length=12,blank=True)

    
    def save(self, *args, **kwargs):
        if self.referral_id == "":
            user_id = (generate_ref_code())
            # user_id = ("SSR"+generate_ref_code())
            self.referral_id = user_id
        super().save(*args, **kwargs)


    def __str__(self):
        return self.user.username


class Prodcut(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    duration = models.IntegerField()
    commission = models.IntegerField()
    product_img = models.ImageField(upload_to="product_img")


upi_choices = (
    ("phonepay","Phonepay"),
    ("paytm","Paytm"),
    ("Gpay","Gpay"),
    ("Tpay","Tpay"),
) 

class upi(models.Model):
   
    select_upi = models.CharField(max_length=50,choices=upi_choices)
    upi_number = models.CharField(max_length=50)

    def __str__(self):
        return self.select_upi
    
status = (
    ("pending","pending"),
    ("accept","accept"),
    ("rejected","rejected"),
   
) 

class recharge(models.Model):
    user = models.ForeignKey(to=Profile,on_delete=CASCADE)
    recharge_amount = models.IntegerField()
    upi = models.ForeignKey(upi,on_delete=CASCADE)
    reference_number = models.CharField(max_length=50)
    # totl_recharge = models.IntegerField(default=0)
    
    status = models.CharField(max_length=50,choices=status,default="pending")

    def __str__(self):
        return self.user.user.username
    


class kyc(models.Model):
    user = models.OneToOneField(to=User,on_delete=CASCADE)
    holder_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
    

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Prodcut,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    


