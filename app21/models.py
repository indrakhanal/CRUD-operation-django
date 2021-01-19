from django.db import models
# Create your models here.


class Customer(models.Model):
    fullname = models.CharField(max_length=100, blank=True, default='')
    mobile = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['fullname']

    def __str__(self):
        return str(self.id)+" | "+self.fullname+" | "+self.mobile+" | "+self.email