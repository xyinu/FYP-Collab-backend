# Generated by Django 4.2.3 on 2024-01-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_ticket_final_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(max_length=80),
        ),
    ]
