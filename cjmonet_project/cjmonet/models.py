from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name

class Painting(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='paintings')
    title = models.CharField(max_length=100, default="no title")
    preview_url = models.CharField(max_length=200, null=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.title

class Sticker(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='stickers')
    title = models.CharField(max_length=100, default="no title")
    image_url = models.CharField(max_length=200, null=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.title
