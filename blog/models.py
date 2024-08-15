from django.db import models


class Notification(models.Model):
    content = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    

class Feedback(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}: {self.message}"
