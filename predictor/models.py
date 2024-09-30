from django.db import models

class ElectrolyteData(models.Model):
    serum_sodium = models.FloatField()
    serum_potassium = models.FloatField()
    serum_calcium = models.FloatField()
    serum_magnesium = models.FloatField()
    bicarbonate = models.FloatField()
    phosphorus = models.FloatField()
    outcome = models.CharField(max_length=50)

    def __str__(self):
        return f"Electrolyte Data - {self.outcome}"
