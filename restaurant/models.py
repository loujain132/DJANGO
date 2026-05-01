from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def _str_(self):
        return self.name


class Table(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()

    def _str_(self):
        return f"Table {self.number}"


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.price for item in self.items.all())