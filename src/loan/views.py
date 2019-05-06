from django.shortcuts import render
from rest_framework import viewsets
from .models import Loan
from .serializers import LoanSerializer
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

# Create your views here.
class LoanView(viewsets.ModelViewSet):
	queryset = Loan.objects.all()
	serializer_class = LoanSerializer

	def create(self, request, *args, **kwargs):
		response = super(LoanView, self).create(request, *args, **kwargs)
		context = {}
		DENIED = "Loan application denied."
		PREAPPROVED = "Loan application pre-approved."
		PROCESSED = "Loan application is currently being processed."
		amount_requested = float(request.data['amount'])
		years_in_business = int(request.data['years'])
		if (amount_requested > 50000 and years_in_business < 1):
			context['status'] = DENIED
		elif (amount_requested < 50000 and years_in_business >= 1):
			context['status'] = PREAPPROVED
		else:
			context['status'] = PROCESSED
		return render(request, "loan/status.html", context)