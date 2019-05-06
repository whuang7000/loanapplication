from django.db import models

# Create your models here.

class Loan(models.Model):
	BUSINESS_TYPES = (
		("FOOD_TRUCK", "Food Truck"),
		("CONSTRUCTION", "Construction"),
		("OTHER", "Other")
	)
	name = models.CharField(max_length=50)
	amount = models.DecimalField(max_digits=100, decimal_places=2)
	business_type = models.CharField(max_length=2, choices=BUSINESS_TYPES, default="FOOD_TRUCK")
	years = models.PositiveIntegerField()

	def __str__(self):
		return self.name