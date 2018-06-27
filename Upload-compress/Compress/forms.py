from django import forms
from Compress.models import Upload

class imageUploadForm(forms.ModelForm):
	class Meta:
		model = Upload
		fields = ('Name','uploadedImage',)

 
		