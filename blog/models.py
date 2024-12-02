from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=50,null=True)
    author= models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name="posts")
    date = models.DateField(max_length=50)
    title = models.CharField(max_length=50)
    excerpt =models.CharField(max_length=50)
    content =models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} {self.author}"




