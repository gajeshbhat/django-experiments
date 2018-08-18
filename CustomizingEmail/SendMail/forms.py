from django import forms
from SendMail.models import SendMessage

class sendMessageForm(forms.ModelForm):
	class Meta:
		model = SendMessage
		fields = ('Message','Email',)

 
		