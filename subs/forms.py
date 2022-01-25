from django import forms
from .models import Subscription

CHOICES =(
    (1,1),
    (3,3),
    (6,6),
    (12, 12),
)

class EditSubscriptionForm(forms.ModelForm):
	period = forms.ChoiceField(choices=CHOICES, required=True, widget=forms.Select(attrs={'class':'form-select'}))

	class Meta:
		model = Subscription
		fields = ('period',)
