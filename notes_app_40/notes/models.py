from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    reminder = models.DateTimeField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')

