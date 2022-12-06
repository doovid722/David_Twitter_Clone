from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
  class Meta(object):
    db_table = 'post'
  name = models.CharField('Name', blank=False, null=False, max_length=14, db_index=True,
  )
  body = models.CharField('Body', blank=True, null=True, max_length=140, db_index=True
  )
  creatd_at = models.DateTimeField('Created DateTime', blank=True, auto_now_add=True
  )
  image = CloudinaryField(
    'image', blank= True, db_index=True
  )

  likes = models.PositiveIntegerField(
    'like', default=0, blank=True, db_index=True
  )
 

  def __str__(self):
    return self.name