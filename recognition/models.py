from django.db import models


class Prediction(models.Model):
    image=models.ImageField(upload_to="")
