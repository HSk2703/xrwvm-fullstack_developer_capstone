# from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
from django.contrib import admin
from .models import CarMake, CarModel

# Register the CarMake and CarModel models with the admin site
admin.site.register(CarMake)
admin.site.register(CarModel)

