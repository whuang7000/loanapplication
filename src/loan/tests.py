from rest_framework.test import APITestCase
from rest_framework import status
from .models import Loan

# Create your tests here.

class LoanPostAPITest(APITestCase):
	
	def test_create_denied_loan(self):
		data = {
			'name': 'Taco Bell',
			'amount': '100000',
			'business_type': 'FOOD_TRUCK',
			'years': '0',
		}
		response = self.client.post('', data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(Loan.objects.count(), 1)
		self.assertContains(response, "denied")

	def test_create_preapproved_loan(self):
		data = {
			'name': 'Taco Bell',
			'amount': '40000',
			'business_type': 'FOOD_TRUCK',
			'years': '5',
		}
		response = self.client.post('', data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(Loan.objects.count(), 1)
		self.assertContains(response, "pre-approved")

	def test_create_processed_loan(self):
		data = {
			'name': 'Taco Bell',
			'amount': '60000',
			'business_type': 'FOOD_TRUCK',
			'years': '5',
		}
		response = self.client.post('', data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(Loan.objects.count(), 1)
		self.assertContains(response, "processed")


