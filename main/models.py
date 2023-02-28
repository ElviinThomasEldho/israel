from django.db import models

class Content(models.Model):
    about = models.CharField("About",max_length=500,null=True)
    email = models.EmailField('Email Address', null=True)
    mobile = models.CharField('Contact Number', max_length=14, null=True)
    address = models.CharField("Address",max_length=500,null=True)
    
    def __str__(self):
        return (str(self.id))

class Service(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField("Title",max_length=255,null=True)
    desc = models.CharField("Description",max_length=500,null=True)
    
    def __str__(self):
        return (str(self.id) + " | " + str(self.title))

class Review(models.Model):
    image = models.ImageField(null=True)
    name = models.CharField("Full Name",max_length=255,null=True)
    occupation = models.CharField("Occupation",max_length=255,null=True)
    dateOfTravel = models.DateField("Date of Travel", null=True)
    title = models.CharField("Title",max_length=255,null=True)
    desc = models.CharField("Description",max_length=500,null=True)
    
    def __str__(self):
        return (str(self.id) + " | " + str(self.name))