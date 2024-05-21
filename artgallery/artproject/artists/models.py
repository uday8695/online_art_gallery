# from django.db import models

# from styles.models import styles
# # Create your models here.

# class Student(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     artist_name = models.CharField(max_length=50)
#     category= models.CharField(max_length=50)
#     style = models.ForeignKey(styles, on_delete=models.CASCADE, related_name='artists')

#     def _str_(self):
#         return f"{self.first_name} {self.last_name} ({self.roll_number})"