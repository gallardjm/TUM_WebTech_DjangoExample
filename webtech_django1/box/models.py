from django.db import models
from storage.models import Storage

class Box(models.Model): #extend django's Model class
	
	#field in the database
    tag = models.CharField(max_length = 100)
    storage = models.ForeignKey(Storage) #f.key for the many-to-one relationship
    
    def __str__(self):
        return self.tag

