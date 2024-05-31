# Product ID: A unique identifier for each product.
# Name: The name of the product (e.g., "Acrylic Paint Set").
# Category: The type of product (e.g., paints, brushes, canvases, easels).
# Brand: The brand name of the product (e.g., Winsor & Newton, Faber-Castell).
# Supplier Name: The name of the supplier.
# Price: The selling price of the product.
# Description: A brief description of the product.
# Image URL: A link to an image of the product.
# Status: Availability status (e.g., in stock, out of stock, discontinued).


from django.db import models

class Artsupplies(models.Model):
    product_id=models.PositiveIntegerField()
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
 
    price= models.PositiveIntegerField()
    description= models.CharField(max_length=50)
    image_url=models.URLField()
    
    def __str__(self):
        return f"{self.product_name} {self.category}"