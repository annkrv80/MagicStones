from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Forma(models.Model):
    name = models.CharField(max_length=50,
                            help_text="Введите форму украшения",
                            verbose_name="Форма украшения")

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.IntegerField(null=True,
                               validators=[MaxValueValidator(200), MinValueValidator(10)],
                               help_text="Введите размер",
                               verbose_name="Размер украшения")

    def __str__(self):
        return str(self.name)


class Accessories(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Введите информацию о фурнитуре",
                            verbose_name="Фурнитура")

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введите статус экземпляра украшения",
                            verbose_name="Статус экземпляра украшения")

    def __str__(self):
        return self.name


class Stone(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите название камня",
                            verbose_name="Название камня")
    description = models.TextField(help_text="Введите информацию о камне",
                                   verbose_name="Описание камня")
    country = models.CharField(max_length=100,
                               help_text="Информация о стране происхождения",
                               verbose_name="Страна происхождения")
    photo = models.ImageField(upload_to='images',
                              help_text="Введите фото камня",
                              verbose_name="Фото камня",
                              null=True, blank=True)

    def __str__(self):
        return self.name


class Jewelry(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите название украшения",
                            verbose_name="Название украшения")
    size = models.ManyToManyField('Size', null=True, blank=True,
                                  help_text="Выберите размер(размеры)",
                                  verbose_name="Размер(размеры) украшения")
    forma = models.ForeignKey('Forma', on_delete=models.CASCADE,
                              help_text="Введите форму украшения",
                              verbose_name="Форма украшения")
    stone = models.ManyToManyField('Stone',
                                   help_text="Выберите камни",
                                   verbose_name="Камни в украшении")
    accessories = models.ForeignKey('Accessories', on_delete=models.CASCADE,
                                    help_text="Выберите фурнитуру",
                                    verbose_name="Фурнитура украшения")
    description = models.TextField(max_length=1000,
                                   help_text="Введите описание украшения",
                                   verbose_name="Описание украшения")
    price = models.DecimalField(decimal_places=2, max_digits=7,
                                help_text="Введите цену украшения",
                                verbose_name="Цена (руб.)")
    photo = models.ImageField(upload_to='images',
                              help_text="Введите фото украшения",
                              verbose_name="Фото")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jewerly-detail', args=[str(self.id)])

    def display_stone(self):
        return ', '.join([stone.name for stone in self.stone.all()])

    display_stone.short_description = 'Камни в украшении'


class JewelryInstance(models.Model):
    jewelry = models.ForeignKey('Jewelry', on_delete=models.CASCADE, null=True)
    inv_num = models.CharField(max_length=20, null=True,
                               help_text="Введите инвентарный номер экземпляра",
                               verbose_name="Инвентарный номер")
    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=True, help_text="Изменить состояние экземпляра",
                               verbose_name="Статус экземпляра украшения")
    due_back = models.DateField(null=True, blank=True,
                                help_text="Введите конец срока статуса",
                                verbose_name="Дата окончания срока статуса")
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True, verbose_name="Заказчик",
                                 help_text="Выберите заказчика")

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s  %s  %s' % (self.inv_num, self.jewelry, self.status)


