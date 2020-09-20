# Generated by Django 3.1.1 on 2020-09-20 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200920_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Заказчик', 'verbose_name_plural': 'Заказчики'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer', verbose_name='Заказчик'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Для дома', 'Для дома'), ('Для улицы', 'Для улицы')], max_length=200, null=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Наименование товара'),
        ),
    ]
