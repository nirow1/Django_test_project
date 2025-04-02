from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length= 200, blank=False)
    completed = models.BooleanField(default=False, blank=False)
    deadline_day = models.DateTimeField(null=True)


class ShoppingList(models.Model):
    name = models.CharField(max_length=50, blank= False)

    def __str__(self):
        return self.name


class Item(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=100, blank=False)
    """unit = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField(default=1)"""

    def __str__(self):
        return self.name

