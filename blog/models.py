from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse("blog", kwargs={"pk": self.pk})
    
    # its best practice to add the above two methods to every model