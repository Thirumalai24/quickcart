from django.db import models
import datetime
import os 

# save filename with time
def getFileName(request,filename):
    now_time = datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)


class Category(models.Model):
    name = models.CharField(max_length=150,null=False, blank=False)
    image = models.ImageField(upload_to='getFileName', blank=True, null=True)
    description = models.TextField(max_length=500,null=False, blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending =models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') 
    name = models.CharField(max_length=150,null=False, blank=False)
    vendor = models.CharField(max_length=150,null=False, blank=False)
    image = models.ImageField(upload_to='getFileName', blank=True, null=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=1000,null=False, blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending =models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name