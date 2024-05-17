# Generated by Django 5.0.6 on 2024-05-17 09:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('course', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('entry_scheme', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('intake', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('sponsorship', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=255)),
                ('residence', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
            ],
        ),
    ]
