from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100) # input text field
    body = models.TextField() # textarea
    created_at = models.DateTimeField(auto_now_add=True)


# create/code model
# create migration file for the changes in models.py file # py manage.py makemigrations
# run migration files # py manage.py migrate

# ORM (Object Relational Mapping in django)