from django.db import models

#Create Product Model

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.0, null=False, blank=False)
    
    def __str__(self):
        return self.name
    

    @property
    def get_discounted_price(self):

        d_price = f'{self.price * 0.9:.2f}'

        # return number version of d_price
        return float(d_price)
    