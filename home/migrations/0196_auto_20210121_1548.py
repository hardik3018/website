# Generated by Django 3.1.4 on 2021-01-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0195_auto_20210121_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='general_funding_application',
            field=models.TextField(blank=True, max_length=3000, verbose_name='What humanitarian issues is your community addressing?'),
        ),
    ]
