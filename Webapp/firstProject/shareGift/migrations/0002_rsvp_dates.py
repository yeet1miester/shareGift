# Generated by Django 3.0.1 on 2021-09-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareGift', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='dates',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
