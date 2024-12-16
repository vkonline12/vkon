from django.db import models

# Create your models here.
class Web_Project(models.Model):
    title=models.CharField(max_length=250,unique=True)
    img=models.ImageField(upload_to='images',blank=True)
    contacts=models.TextField(max_length=500)
    description=models.TextField(blank=True)
    mode=models.CharField(max_length=250)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return '{}'.format(self.title)

class website(models.Model):
    name=models.CharField(max_length=250,unique=True)
    address=models.TextField(blank=True)
    contact=models.CharField(max_length=10)
    email=models.EmailField(max_length=250)
    type_of_website=models.TextField(max_length=1000)
    date = models.DateTimeField(null=True)
    def __str__(self):
        return '{}'.format(self.name)

class myweb(models.Model):
    title_of_site=models.CharField(max_length=250,unique=True)
    imge = models.ImageField(upload_to='images', blank=True)
    details=models.TextField(blank=True)
    description = models.TextField(blank=True)
    mode = models.CharField(max_length=250)
    date = models.DateTimeField(null=True)
    def __str__(self):
        return '{}'.format(self.title_of_site)