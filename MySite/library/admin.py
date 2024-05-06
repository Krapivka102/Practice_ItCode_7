from django.contrib import admin
from library import models

admin.site.register(models.User)
admin.site.register(models.Book)
admin.site.register(models.Genre)

