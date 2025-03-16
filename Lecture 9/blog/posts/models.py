from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255) # 1 row text field
    body = models.TextField() # multiple row text field / block
    created_at = models.DateTimeField(auto_now_add=True) # automatically stores time value
