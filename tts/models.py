from django.db import models

class MP3File(models.Model):
    title = models.CharField(max_length=100)
    mp3 = models.FileField(upload_to='mp3_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title