from django.db import models


# Author model represents a book author.
# One author can have multiple books.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model represents books written by authors.
# Each book belongs to one author.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'   # Allows accessing books from author
    )

    def __str__(self):
        return self.title
