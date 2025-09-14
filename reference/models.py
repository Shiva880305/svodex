# reference/models.py

from django.db import models
from ckeditor.fields import RichTextField


class Reference(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='references/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ReferenceImage(models.Model):
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='references/gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Image for {self.reference.title}'


class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50)
    description = models.TextField()
    content = RichTextField(blank=True, null=True) # Nové pole pro detailní text
    # ... další pole

    def __str__(self):
        return self.title

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service_gallery/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.service.title}"


class Certificate(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='certificates/')
    image = models.ImageField(upload_to='certificates/previews/', blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Stat(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title