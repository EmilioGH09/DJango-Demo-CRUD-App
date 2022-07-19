from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    class Meta:  
        db_table = "drinks"  

    def __str__(self):
        return self.name

