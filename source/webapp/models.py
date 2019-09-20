from django.db import models

status_choices = [('different', 'разное'),
                  ('vegetables', 'овощи'),
                  ('dairy', 'молочное'),
                  ('toys', 'игрушки'),
                  ('seafood', 'морепродукты')]


class Product(models.Model):
    name_of_product = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='описание')
    date = models.DateField(max_length=3000, null=False, blank=False, verbose_name='Дата')
    count = models.IntegerField(verbose_name='остаток')
    status = models.CharField(max_length=20, verbose_name='Тема', default=status_choices[0][0], choices=status_choices)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.description
