# Uncomment the following imports before adding the Model code

# from django.db import models
# from django.utils.timezone import now
# from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
from django.db import models

# CarMake model to store car makes (e.g., Toyota, Ford)
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  # Return the name as the string representation



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# CarModel model to store car models (e.g., Corolla, Mustang)
class CarModel(models.Model):
    car_make = models.ForeignKey('CarMake', on_delete=models.CASCADE)  # Many-to-One relationship to CarMake
    dealer_id = models.IntegerField()  # Dealer ID from the Cloudant database
    name = models.CharField(max_length=100)  # Model name (e.g., Corolla, Mustang)
    
    # Choices for car type
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')  # Car type with choices
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )  # Car year with validation

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"  # Return make, model, and year as the string representation

