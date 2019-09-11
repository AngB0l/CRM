from django.db import models
from django.contrib.auth.models import User

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
     company = models.CharField(max_length=80)
     field = models.CharField(max_length=30, choices=FIELD, default=MARBLE,)
     remarks = models.TextField()
     address = models.CharField()
     area =  models.CharField()
     city =  models.CharField(max_length=20)
     country = models.CharField(max_length=20)
     website = models.URLField()
     phone = models.IntegerField() #length
     quarryowners = models.IntegerField(max_length=1)
     pending = models.CharField(max_length=100)
     def __str__(self):
         return self.company

class Contact(models.Moldel):
     date = models.DateField()
     user = models.ForeignKey(User, on_delete=models.PROTECT)
     company = models.ForeignKey(Company, on_delete=models.PROTECT)
     comments = models.TextField()
     reminder = models.DateTimeField()
     def __str__(self):
        return self.id

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
     area = models.CharField()
     country = models.CharField(max_length=20)
     name = models.CharField(max_length=30)
     type = models.CharField(max_length=20, choices=TYPE_OF_MATERIAL, default=MARBLE,)
     colorPrimary = models.CharField(max_length=20)
     colorSecondary = models.CharField(max_length=20)
     def __str__(self):
        return self.name