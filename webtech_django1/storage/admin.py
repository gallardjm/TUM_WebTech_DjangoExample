from django.contrib import admin
from storage.models import Storage

admin.site.register(Storage) #Hook the models to the admin site
