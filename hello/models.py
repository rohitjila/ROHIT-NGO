from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    Name= models.CharField(max_length=255)
    Full_Address=models.TextField(max_length=300)
    image=models.ImageField(upload_to='images/')
    self_image=models.ImageField(upload_to='images/')
    votes_total=models.IntegerField(default=1)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return self.Name

    def summary(self):
        return self.Full_Address[:100]

     


    


