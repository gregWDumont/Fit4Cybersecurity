# Generated by Django 2.2.7 on 2019-11-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "1000_surveyuserfeedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="surveyuser",
            name="country_code",
            field=models.CharField(default="SE", max_length=2),
        ),
    ]
