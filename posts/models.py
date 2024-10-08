from django.db import models
from django.contrib.auth.models import User

# Create your models here. They model data, and each type of data has its own table in the database. Migrations turns it into a database table
class Post(models.Model):
    title = models.CharField(max_length=75) ### Charfield is a different type of model
    body = models.TextField() ### Charfield is a different type of model
    slug = models.SlugField() ### Part of the URL that identifies the post
    date = models.DateTimeField(auto_now_add=True) ### Auto now add automatically records date and time every time user adds another post (title body and slug)
    banner = models.ImageField(default='fallback.png', blank=True) ### Blank = true means photo not required.
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None) ### Connecting author as foreign key from Users table. Cascade means if user is deleted, so are posts

    def __str__(self):
        return self.title

### title and body are fields of the model. Each field is specified as a class attribute, and each attribute maps to a database column.