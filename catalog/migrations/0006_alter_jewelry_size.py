# Generated by Django 5.0 on 2023-12-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_size_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='size',
            field=models.ManyToManyField(blank=True, help_text='Выберите размер(размеры)', null=True, to='catalog.size', verbose_name='Размер(размеры) украшения'),
        ),
    ]
