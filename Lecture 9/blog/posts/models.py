from django.db import models


class BlogPost(models.Model): # id, title, body, created_at
    title = models.CharField(max_length=100) # input text field
    body = models.TextField() # textarea
    created_at = models.DateTimeField(auto_now_add=True) # time stored when object is created
    # updated_at = models.DateTimeField(auto_now=True) # time stored when object is updated/edited

    # magic method __magicmethods__
    def __str__(self):
        return f'{self.title} | {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}'

# migration file

# create/code model
# create migration file for the changes in models.py file # py manage.py makemigrations
# run migration files # py manage.py migrate

# ORM (Object Relational Mapping in django)

# MySQL
# PostgreSQL # production
# SQLite # development
# Oracle


# Mongodb