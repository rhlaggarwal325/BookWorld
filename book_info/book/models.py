from django.db import models

# Create your models here.

class Book(models.Model):
    genres = (
        ('Fantasy','Fantasy'),
        ('Science Fiction','Science Fiction'),
        ('Action','Action'),
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Horror','Horror'),
        ('Romance','Romance'),
        ('History','History'),
        ('Literary','Literary'),
        ('Biography', 'Biography')
    )
    languages = (
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Arabic', 'Arabic'),
        ('French', 'French'),
        ('Persian', 'Persian'),
        ('Sanskrit', 'Sanskrit')
    )
    name = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 200, choices = genres)
    language = models.CharField(max_length = 200, choices = languages)

    def __str__(self):
        return self.name