from django import forms
from .models import *


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('comment_text', )


class ImageForm(forms.ModelForm):
	class Meta:
		model = Images
		fields = ['image_file']