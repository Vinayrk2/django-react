from django.db import models
# register model
class User(models.Model):
    fname = models.CharField(max_length=50, null=False)
    lname = models.CharField(max_length=50, null=False)
    # Define gender as a CharField with choices
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    address = models.TextField(null=False)
    email = models.EmailField(max_length=200, unique=True, null=False)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Login(models.Model):
    email = models.EmailField(max_length=200, unique=True, null=False)
    password = models.CharField(max_length=256)
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    def __str__(self):
        return self.name