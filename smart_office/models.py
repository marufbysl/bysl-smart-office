from django.db import models

# Create your models here.
from blog.models import BaseModel
from apps.models import AppFeature
class Fqa(BaseModel):
    question=models.TextField()
    answer=models.TextField()
    feature_id=models.ForeignKey("apps.AppFeature",verbose_name=("APP FEATURE"),on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.question

class Customer(BaseModel):
    name=models.CharField(max_length=50)
    description=models.TextField()
    logo=models.ImageField(upload_to="static/images", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name

class CustomerReview(BaseModel):
    customer_id =models.ForeignKey(Customer,verbose_name=("Customer"),on_delete=models.CASCADE)
    review = models.TextField()

    def __str__(self):
        return self.review
    
class ContactMessage(BaseModel):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    message=models.TextField()

    def __str__(self):
        return self.first_name

class Subscription(BaseModel):
    email=models.EmailField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.email