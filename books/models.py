from django.db import models

# Create your models here.
# 책 관련
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

# 펼친이
class Author(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

# 출판사 관련
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name