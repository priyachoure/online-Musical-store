from django.db import models

# Create your models here.
"static model"


class Instrument(models.Model):
    # id: int
    # name: str
    # price: float
    # desc: str
    # img: str
    "dynamic model"
    name = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
