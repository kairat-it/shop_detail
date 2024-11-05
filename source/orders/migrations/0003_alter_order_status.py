# Generated by Django 5.0.6 on 2024-11-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderpart_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('in_process', 'В обработке'), ('completed', 'Выполнен')], default='in_process', max_length=20, verbose_name='Статус заказа'),
        ),
    ]
