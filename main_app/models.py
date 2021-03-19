from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# garfield = Cat('Garfield', 'Tabby', 40, 'he is mean to Oddy')

# print(garfield)