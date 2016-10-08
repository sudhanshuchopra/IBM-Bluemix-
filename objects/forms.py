from django import forms
from .models import visobjects
class searchform(forms.ModelForm):
	class Meta:
		model=visobjects
		fields=['image_pic']