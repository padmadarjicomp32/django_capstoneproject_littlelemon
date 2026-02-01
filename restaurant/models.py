from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)                 # Name of the person
    price = models.DecimalField(max_digits=10, decimal_places=2)                    # Number of guests
    inventory = models.IntegerField(max_length=5)

    def __str__(self):
        return f"{self.title} - {str(self.price)} - {str(self.inventory)}"

class Booking(models.Model):
    name = models.CharField(max_length=255)                 # Name of the person
    no_of_guests = models.IntegerField()                    # Number of guests
    booking_date = models.DateTimeField()                   # Booking date and time

    def __str__(self):
        return f"{self.name} - {str(self.booking_date)} - {str(self.no_of_guests)}"