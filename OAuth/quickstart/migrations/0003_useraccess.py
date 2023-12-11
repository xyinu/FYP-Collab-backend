# Generated by Django 4.2.3 on 2023-12-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_faq_ticket_thread_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccess',
            fields=[
                ('email', models.CharField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('TA', 'TA'), ('Prof', 'Prof')], default='TA', max_length=40)),
            ],
        ),
    ]