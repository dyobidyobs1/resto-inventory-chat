from django.db import models

# Create your models here.

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
        return self.branch

class MOP(models.Model):
    modeofp = models.CharField(max_length=50)

    def __str__(self):
        return self.modeofp

class FoodInventory(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    prod_name = models.CharField(max_length=255)
    prod_type = models.ForeignKey(ProdType, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.FloatField(max_length=10)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.prod_name}'
        # return f'{self.prod_name} | {self.branch}'

class DailySales(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    prod_name = models.ForeignKey(FoodInventory, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer = models.CharField(max_length=255)
    mop = models.ForeignKey(MOP, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
       return f'SO-{self.id}'