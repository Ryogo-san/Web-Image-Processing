from django.db import models


class InputImage(models.Model):
    image = models.ImageField(upload_to="")
