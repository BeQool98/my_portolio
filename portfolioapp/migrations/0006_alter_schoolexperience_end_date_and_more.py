# Generated by Django 4.2 on 2023-07-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0005_projects_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolexperience',
            name='end_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schoolexperience',
            name='start_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
