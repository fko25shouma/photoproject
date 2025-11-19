from django.db import models

class Memo(models.Model):
    content12 = models.TextField(max_length=300)
    nickname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ti
