from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_created=True, auto_now_add=True,null=False, blank=False)
    photo = models.ImageField(upload_to='Blog', null=True, blank=True)
    def __str__(self):
        return self.title