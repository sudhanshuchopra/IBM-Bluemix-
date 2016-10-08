from django.db import models

# Create your models here.
class visobjects(models.Model):
	image_pic = models.ImageField(upload_to = 'profile_pics/')

class tags(models.Model):
	tags_value=models.CharField(max_length=50,null=True)
	parent=models.ForeignKey(visobjects,related_name='attr')