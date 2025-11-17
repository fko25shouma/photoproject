from django.db import models

class Memo(models.Model):
    title = models.CharField(max_length=300)
    nickname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ti
