from django.test import TestCase
from .views import cal_amount
from .models import Product 
from .url import cal_amount

class ViewsTestCase(TestCase):
	def test_index_loads_properly(self):
		response = self.client.get('http://localhost:8000/billing/')
		self.assertEqual(response.status_code, 200)

class TestCalculateAmount(TestCase):
	def test_totalamount(self):
		self.result = [
			(["CH1","AP1","AP1","AP1","MK1"],16.61),
			(["CH1","AP1","CF1","MK1"],20.34),
			(["AP1","MK1"],10.75),
			(["CF1","CF1"],11.23),
			(["CH1","AP1","AP1","AP1"],16.61),
			(["AP1","OM1","CH1","CF1","MK1"],16.61),
			(["CH1","AP1","AP1","AP1","MK1"],21.03),
			(["CH1","AP1","AP1","AP1","OM1","CF1","CF1","MK1"],24.78),
			(["CH1","AP1","AP1","OM1","CF1","CF1","MK1"],24.03),
			(["AP1","AP1","AP1","AP1"],18.00)
		]
		count_of_items = {"AP1":0,"CF1":0,"CH1":0,"OM1":0,"MK1":0}
		products = Product.objects.all()
		for items,amount_expected in self.result:
			for i in items:
				if i == "AP1":
					count_of_items['AP1']+=1
				if i == "CH1":
					count_of_items["CH1"]+=1
				if i == "CF1":
					count_of_items["CF1"]+=1
				if i == "OM1":
					count_of_items["OM1"]+=1
				if i== "MK1":
					count_of_items["MK1"]+=1
			print(count_of_items)
			response = self.client.get('http://localhost:8000/billing/bill/')
			self.assertEqual(amount_expected,response["total_amount"])