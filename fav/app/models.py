from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
class  Quote(models.Model):
    line = models.TextField(blank = True)
    categories = models.ForeignKey(Categories,on_delete = models.CASCADE, related_name = "category")
    key = models.UUIDField(primary_key = True, default= uuid.uuid4, editable = False)
    def __str__(self):
        return self.line

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    dialogue = models.TextField(blank = True) 
    quotes = models.ForeignKey(Quote, on_delete = models.CASCADE , related_name= 'quota',null =True)


class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete = models.CASCADE)
    replied = models.TextField(blank = True)

class Favourite(models.Model):
    favourite_item = models.ForeignKey(Quote,on_delete = models.CASCADE, related_name = 'quote', null = True )
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'user', null = True)