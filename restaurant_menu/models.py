# To run Database Model use following command in terminal: python manage.py makemigrations
# To create the Database off those models use: python manage.py migrate
from django.db import models
from django.contrib.auth.models import User  # imports user database model

# A Tuple of Tuples - second word in each tuple is used on front-end, first param is used by code
MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("mains", "Mains"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


# All database models - many-to-one relationship with User
class Item(models.Model):
    # set unique to true to ensure we have unique meals in database
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 2 decimal points
    meal_category = models.CharField(max_length=200, choices=MEAL_TYPE)
    # If you use CASCADE when a User is deleted then all meals they created is also Deleted.
    # If you want to not delete then use models.PROTECT, if you want to be able to set value to null on items then use
    # models.SET_NULL
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)  # auto_now_add adds value when Item is created
    date_updated = models.DateTimeField(auto_now=True)  # auto_now updates value when Item is edited

    def __str__(self):
        return self.meal
