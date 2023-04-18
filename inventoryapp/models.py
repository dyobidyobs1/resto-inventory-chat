from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import locale
import uuid
# locale.setlocale(locale.LC_ALL, 'fil-PH')

# Create your models here.
def create_rand_id():
        from django.utils.crypto import get_random_string
        return get_random_string(length=13, 
            allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')


class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size

class ProdType(models.Model):
    prod_type = models.CharField(max_length=50)

    def __str__(self):
        return self.prod_type

class Branch(models.Model):
    branch = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.branch} - {self.id}'

class MOP(models.Model):
    modeofp = models.CharField(max_length=50)

    def __str__(self):
        return self.modeofp

class FoodInventory(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    prod_name = models.CharField(max_length=255)
    prod_type = models.ForeignKey(ProdType, on_delete=models.CASCADE)
    description = models.TextField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.FloatField(max_length=10)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="foods/%Y/%m/%d/")

    def __str__(self):
        return f'{self.prod_name}'
        # return f'{self.prod_name} | {self.branch}'
    
    def new_price(self):
        locale.setlocale(locale.LC_ALL, 'fil-PH')
        return locale.currency(self.price, grouping=True)

class DailySales(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    prod_name = models.ForeignKey(FoodInventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    mop = models.ForeignKey(MOP, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reference_number = models.CharField(max_length=13, editable=False, null=True, blank=True, 
        default=create_rand_id)

    def __str__(self):
       return f'SO-{self.id}'

    def price(self):
        locale.setlocale(locale.LC_ALL, 'fil-PH')
        return locale.currency(self.amount, grouping=True)

class OrderCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    branch = models.CharField(max_length=50, default="Mandaluyong")
    product_name = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cart_reference = models.CharField(max_length=50, null=True, blank=True)

    def price(self):
        locale.setlocale(locale.LC_ALL, 'fil-PH')
        return locale.currency(self.amount, grouping=True)
    
    def __str__(self):
        return f"Cart for User {self.user} | {self.cart_reference} | {self.id}"
    
class OrderProcess(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    product_id = ArrayField(models.CharField(max_length=255))
    total_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    name_buyer = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    # mop = models.ForeignKey(MOP, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=255, editable=False, null=True, blank=True,
        default=create_rand_id)


    def __str__(self):
        return self.reference_number
    
    def price(self):
        locale.setlocale(locale.LC_ALL, 'fil-PH')
        return locale.currency(self.total_amount, grouping=True)
