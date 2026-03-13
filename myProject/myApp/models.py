from django.db import models


class AboutModel(models.Model):
    name = models.CharField( max_length=100, null=True)
    Address=models.CharField( max_length=50, null=True)
    Age= models.CharField( max_length=10, null=True)
    date_of_birth=models.DateField(null=True)
    Education= models.CharField( max_length=50, null=True)
    department=models.CharField( max_length=50, null=True)
    image=models.ImageField(
     upload_to="Pictures",  null=True)


    def __str__(self):
        return self.name
    
    

