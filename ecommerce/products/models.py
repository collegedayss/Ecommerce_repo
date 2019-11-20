# import random
# import os
from django.db import models


# def get_filename_ext(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext


# def upload_image_path(instance, filename):
#    # print(instance)
#    # print(filename)
#     new_filename = random.randint(1, 123124)
#     name, ext = get_filename_ext(filename)
#     final_filename = f'{new_filename}{ext}'
#     return f"products/{new_filename}/{final_filename}"


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    image = models.FileField(
        upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
