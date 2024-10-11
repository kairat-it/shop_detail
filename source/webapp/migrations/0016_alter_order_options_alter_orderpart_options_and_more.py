# Generated by Django 5.0.6 on 2024-10-10 09:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_alter_orderpart_quantity_alter_orderpart_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('id',), 'verbose_name': 'Заказ оформления', 'verbose_name_plural': 'Заказы оформления'},
        ),
        migrations.AlterModelOptions(
            name='orderpart',
            options={'ordering': ('id',), 'verbose_name': 'Проданный товар', 'verbose_name_plural': 'Проданные товары'},
        ),

        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(blank=True, null=True, verbose_name='Адрес доставки'),
        ),
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Оплачено'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_on_get',
            field=models.BooleanField(default=False, verbose_name='Оплата при получении'),
        ),
        migrations.AddField(
            model_name='cart',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
        ),
        migrations.AddField(
            model_name='order',
            name='requires_delivery',
            field=models.BooleanField(default=False, verbose_name='Требуется доставка'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='В обработке', max_length=50, verbose_name='Статус заказа'),
        ),
        migrations.AddField(
            model_name='orderpart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None, verbose_name='Дата продажи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderpart',
            name='name',
            field=models.CharField(default=None, max_length=150, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderpart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа'),
        ),
        migrations.AlterField(
            model_name='orderpart',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='orderpart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
