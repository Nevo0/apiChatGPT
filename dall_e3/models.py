from django.db import models

class DallE3File(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='img/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title