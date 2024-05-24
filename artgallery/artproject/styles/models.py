from django.db import models

# Create your models here.
class Styles(models.Model):
    style_type= models.CharField(max_length=50)
    period=models.PositiveIntegerField()
    origin= models.CharField(max_length=50)
    key_characteristics= models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
    depth= models.CharField(max_length=50)
    balance= models.CharField(max_length=50)
    complexity= models.CharField(max_length=50)
    description=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.style_type} {self.theme}"
    

# style_type: The name of the art style (e.g., Impressionism, Cubism).
# Period: The time period during which the art style was most prominent (e.g., 1860-1900).
# Origin: The geographic region or country where the art style originated.
# Key Characteristics: Distinctive features or techniques associated with the art style (e.g., use of light and color, abstract forms).
# Themes: Common themes or subjects in artworks of this style (e.g., nature, urban life, abstract concepts).
