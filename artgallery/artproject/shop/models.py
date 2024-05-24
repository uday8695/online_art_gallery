from django.db import models


# Create your models here.

class Shop(models.Model):
    product_id= models.PositiveIntegerField()
    product_name = models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    artist_id= models.PositiveIntegerField()
    artist_name = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)
    dimensions= models.CharField(max_length=50)
    brand=models.CharField(max_length=50)
    supplier_id= models.PositiveIntegerField()
    supplier_name = models.CharField(max_length=50)
    price= models.CharField(max_length=50)
    stock_quantity=models.PositiveIntegerField()
    status=models.CharField(max_length=10)
    description=models.CharField(max_length=50)
    image_url=models.URLField()

    def __str__(self):
        return f"{self.title}"
    
# Product ID: A unique identifier for each product.
# Name: The name of the product (e.g., artwork title, type of art supplies).
# Category: The type of product (e.g., painting, sculpture, paintbrushes, canvases).
# Artist ID: A unique identifier for the artist (if applicable).
# Artist Name: The name of the artist (if applicable).
# Medium: The materials or technique used (e.g., oil on canvas, watercolor, acrylic).
# Dimensions: The size of the artwork (e.g., height, width, depth).
# Brand: The brand name of the art supplies (if applicable).
# Supplier ID: A unique identifier linking to the supplier.
# Supplier Name: The name of the supplier.
# Price: The selling price of the product.
# Stock Quantity: The current stock level.
# Status: Availability status (e.g., available, sold, out of stock).
# Description: A brief description of the product.
# Image URL: A link to an image of the product.