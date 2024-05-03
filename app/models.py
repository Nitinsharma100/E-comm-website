from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=20, null=True, blank=True)
    confirm_password = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.name
