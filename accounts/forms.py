from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
		# OR we can define which attributes of model should be filled in form
		# fields = ['customer', 'product']