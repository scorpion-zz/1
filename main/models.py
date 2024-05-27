from django.db import models


class Avtor(models.Model):
    name = models.CharField(max_length=255)
    familia = models.CharField(max_length=255)
    date = models.DateField()
    foto = models.ImageField()

    def __str__(self):
        return f'{self.name} {self.familia}'

class Book(models.Model):
    name = models.CharField(max_length=255)
    data_of_public = models.DateField()
    short_description = models.TextField()
    image = models.ImageField()

    autor = models.ForeignKey(
        "Avtor",
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f'{self.name} '



# class Reader(models.Model):     # пользователь
#     name = models.CharField(max_length=255)
#     familia = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f'{self.name} {self.familia}'

class Review(models.Model):
     review = models.TextField()
     deta = models.DateField()
     book = models.ForeignKey('Book', on_delete=models.CASCADE)

     def __str__(self):
         return f'{self.id} {self.book} '