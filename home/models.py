from django.db import models

# Create your models here.
class content(models.Model):
    content_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to="home/images",default="")
    slug = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.title