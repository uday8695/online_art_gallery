from django.db import models
from datetime import datetime

# Create your models here.

class Artists(models.Model):
    Artist_id=models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    artist_age = models.CharField(max_length=50)
    category= models.CharField(max_length=50)
    experience= models.PositiveIntegerField()
    earnings= models.CharField(max_length=50)
    no_of_drawings_made=models.PositiveIntegerField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
