# Generated by Django 4.2.3 on 2024-01-05 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_faq_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]