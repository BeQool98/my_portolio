# Generated by Django 4.2 on 2023-08-01 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0006_alter_schoolexperience_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('msg_body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
