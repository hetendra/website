from django import forms
from .models import Post

class PostForm(forms.ModelForms):
	class Meta:
		model = Post
		fields = ('name','email', 'subject', 'message')

		widget = {
			'title': form.TextInput(attrs={'class': 'form-control'})
			'email': form.TextInput(attrs={'class': 'form-control'})
			'subject': form.TextInput(attrs={'class': 'form-control'})
			'message': form.TextInput(attrs={'class': 'form-control'})

		}