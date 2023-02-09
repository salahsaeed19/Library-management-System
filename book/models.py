from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    cover_photo = models.ImageField(upload_to="service/covers/", null=True)
    book_file = models.FileField(upload_to="service/files/", null=True)
    
    def __str__(self):
        return self.name

