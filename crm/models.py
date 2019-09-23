from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Company(models.Model):
     ARCHITECT = 'AR'
     COMMERCE = 'CM'
     CONSTRUCTOR = 'CN'
     DESIGNER = 'DE'
     LANDSCAPE = 'LS'
     MARBLE = 'MA'
     FIELD = [
        (ARCHITECT, 'Architect'),
        (COMMERCE, 'Commerce'),
        (CONSTRUCTOR, 'Constructor'),
        (DESIGNER, 'Designer'),
        (LANDSCAPE, 'Landscape'),
        (MARBLE, 'Marble'),
     ]
     company = models.CharField(max_length=50)
     field = models.CharField(max_length=2, choices=FIELD, default=MARBLE,)
     remarks = models.TextField(blank=True)
     address = models.CharField(max_length=50, blank=True)
     area =  models.CharField(max_length=50, blank=True)
     city =  models.CharField(max_length=20, blank=True)
     country = models.CharField(max_length=20)
     website = models.URLField(blank=True)
     phone = models.IntegerField(blank=True)
     pending = models.CharField(max_length=100, blank=True)
     def __str__(self):
         return self.company
     def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk':self.pk})

class Contact(models.Model):
     date = models.DateField()
     user = models.ForeignKey(User, on_delete=models.PROTECT)
     company = models.ForeignKey(Company, on_delete=models.PROTECT)
     comments = models.TextField()
     reminder = models.DateTimeField(blank=True, null=True)
     def __str__(self):
        return self.comments
     def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk':self.pk})

class ContactDetails(models.Model):
     fname = models.CharField(max_length=20)
     lname = models.CharField(max_length=20)
     position = models.CharField(max_length=20)
     email = models.EmailField()
     company = models.ForeignKey(Company, on_delete=models.PROTECT)
     def __str__(self):
         return self.lname

class Quarry(models.Model):
     DOLOMITE = 'DO'
     GRANITE = 'GR'
     LIMESTONE = 'LS'
     MARBLE = 'MA'
     ONYX = 'ON'
     SANDSTONE = 'SA'
     STONE = 'ST'
     TRAVERTINE = 'TR'
     QUARTZ = 'QU'

     TYPE_OF_MATERIAL = [
         (DOLOMITE, 'Dolomite'),
         (GRANITE, 'Granite'),
         (LIMESTONE, 'Limestone'),
         (MARBLE, 'Marble'),
         (ONYX, 'Onyx'),
         (SANDSTONE, 'Sandstone'),
         (STONE, 'Stone'),
         (TRAVERTINE, 'Travertine'),
         (QUARTZ, 'Quartz'),
     ]
     company = models.ForeignKey(Company, on_delete=models.PROTECT)
     area = models.CharField(max_length=50, blank=True)
     country = models.CharField(max_length=20, blank=True)
     name = models.CharField(max_length=30)
     type = models.CharField(max_length=20, choices=TYPE_OF_MATERIAL, default=MARBLE, blank=True)
     colorPrimary = models.CharField(max_length=20)
     colorSecondary = models.CharField(max_length=20, blank=True)
     def __str__(self):
        return self.name
     def get_absolute_url(self):
        return reverse('quarry-detail', kwargs={'pk':self.pk})