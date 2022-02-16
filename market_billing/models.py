from django.db import models

class Product(models.Model):
	product_id = models.CharField(primary_key=True,max_length = 10,default='AP1')
	product_name = models.CharField(max_length=200)
	product_price = models.FloatField(default=0)
	
	def __str__(self):
		return self.product_name

class Discount(models.Model):
	product_id=models.ForeignKey(
        Product, on_delete=models.CASCADE)
	discountID = models.CharField(max_length = 10)
	discount_count = models.IntegerField(default=0)
	dicount_price = models.FloatField(default=0)
