from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, null=True)

    def __str__(self) -> str:
        return self.first_name + ' ' +  self.last_name

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name