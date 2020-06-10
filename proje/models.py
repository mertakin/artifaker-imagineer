from django.db import models

# Create your models here.

class Categories(models.Model):
	category_name = models.CharField(max_length=120, verbose_name="Category")
	category_slug = models.SlugField(max_length=120, verbose_name="Category Slug", unique=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories' 
	
	def __str__(self):
		return self.category_name

class Images(models.Model):
	image_category = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name="Images Category")
	image_file = models.ImageField(blank=True)

	class Meta:
		verbose_name = 'Image'
		verbose_name_plural = 'Images' 
	
class Comment(models.Model):
	comment_images = models.ForeignKey(Images, on_delete=models.PROTECT, verbose_name="Comment Image")
	comment_text = models.TextField(max_length=10000000, verbose_name="Comment")

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'

	def __str__(self):
		return self.comment_text