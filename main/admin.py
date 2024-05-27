from django.contrib import admin

from main.models import Avtor, Book,Review

# Register your models here.
admin.site.register(Avtor)
admin.site.register(Book)
admin.site.register(Review)