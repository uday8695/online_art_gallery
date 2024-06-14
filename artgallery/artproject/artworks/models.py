from django.db import models


class Artworks(models.Model):
    Artwork_id= models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    artist_id= models.PositiveIntegerField()
    artist_name = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)
    dimensions= models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price= models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    status=models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
    
    
# Create your models here.
# Artwork ID: A unique identifier for each piece of art.
# Title: The name of the artwork.
# Artist ID: A unique identifier linking to the artist.
# Artist Name: The name of the artist.
# Medium: The materials or technique used (e.g., oil on canvas, watercolor, sculpture).
# Dimensions: The size of the artwork (e.g., height, width, depth).
# Category: The type of art (e.g., painting, sculpture, drawing).
# Price: The selling price of the artwork.
# Status: Availability status (e.g., available, sold, reserved).
# Description: A brief description of the artwork.
# Image URL: A link to an image of the artwork.
