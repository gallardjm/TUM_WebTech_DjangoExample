from django.db import models

class Storage(models.Model): #extend django's Model class
	
	#field in the database
	name = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.name
