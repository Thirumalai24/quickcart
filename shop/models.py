from django.db import models
from django.contrib.auth.models import User
import datetime
import os 

# Function to generate a unique filename
def getFileName(instance, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{now_time}_{filename}"  # ✅ Unique timestamped filename
    return os.path.join("uploads/", new_filename)  # ✅ Stored inside "uploads/" directory

class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, blank=True, null=True)  # ✅ Use function, not string
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-default,1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') 
    name = models.CharField(max_length=150,null=False, blank=False)
    vendor = models.CharField(max_length=150,null=False, blank=False)
    product_image = models.ImageField(upload_to=getFileName, blank=True, null=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=1000,null=False, blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending =models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name
    
class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  product_qty=models.IntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)
  
  @property
  def total_cost(self):
      return self.product_qty*self.product.selling_price
  
class Favourite(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)