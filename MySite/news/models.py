from django.db import models

class CurrencyRate(models.Model):
    currency_code = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField() # Дата
    change_percent = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.currency_code} - {self.rate} от {self.date}"
    