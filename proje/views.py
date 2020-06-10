from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.conf import settings
import requests

import random
from .models import *
from .forms import *


# Create your views here.

def imageupload(request):
	if request.method == 'POST':
		if 'fileupload' in request.POST:
			form = ImageForm(request.POST, request.FILES)
			if form.is_valid():
				data = form.save(commit=False)
				data.image_file = request.FILES['image_file']
				data.image_category = Categories.objects.order_by('?').first()
				data.save()
				response = redirect('/review/%s' % data.image_file)
				return response

		elif 'url_upload' in request.POST:
			file_path = (settings.MEDIA_ROOT)
			image_url = request.POST.get('image_file')

			ext = image_url.split('.')[-1]

			chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
			file_name = ''.join((random.choice(chars)) for x in range(6))
			file = str(file_name) + '.' + str(ext)

			r = requests.get(image_url)

			with open(file_path + file, 'wb') as f:
				f.write(r.content)
			f.close()

			form = ImageForm(request.POST)
			if form.is_valid():
				form.cleaned_data
				data = form.save(commit=False)
				data.image_file = file
				data.image_category = Categories.objects.order_by('?').first()
				data.save()
				response = redirect('/review/%s' % data.image_file)
				return response
				
			# print (form.errors)
			return render(request, 'index.html', {})

	else:
		raise PermissionDenied


def index(request):
	images = Images.objects.all().order_by('-id')
	category = Categories.objects.all()

	context = {
	'Title': 'Home Page',
	'images' : images,
	'categories': category,
	}
	return render(request, 'index.html', context)


def category(request, category):
	images = Images.objects.all().filter(image_category__category_slug=category).order_by('-id')
	category_select = Categories.objects.get(category_slug=category)
	category = Categories.objects.all()

	context = {
	'Title': '%s Images' % category_select,
	'images' : images,
	'categories': category,
	'category_select': category_select,
	}
	return render(request, 'category.html', context)


def review(request, image):
	# images = Images.objects.get(image_file=image)
	images = get_object_or_404(Images, image_file=image)
	comment_select = Comment.objects.filter(comment_images__image_file=images.image_file)
	category_select = Categories.objects.get(category_slug=images.image_category.category_slug)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.comment_images = images
			data.comment_text = request.POST.get('comment_text')
			data.save()
			messages.success(request, 'Comment added.')

	context = {
	'Title': '%s Images' % images.image_file,
	'categories': category,
	'images': images,
	'comment': comment_select,
	'category_select': category_select,
	}
	return render(request, 'review.html', context)


