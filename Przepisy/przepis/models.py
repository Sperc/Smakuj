from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


class Category(models.Model):
    category_name = models.CharField(max_length=250)
    category_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('index')


    def __str__(self):
        return self.category_name

class Dish(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    dish_logo = models.FileField()
    dish_receipe = models.TextField(max_length=5000)
    dish_title = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('index')


    def __str__(self):
        return self.dish_title
