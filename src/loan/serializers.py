from rest_framework import serializers
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
	class Meta:
		model = Loan
		fields = (
			'id',
			'name',
			'amount',
			'business_type',
			'years'
		)