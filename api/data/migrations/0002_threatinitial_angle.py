# Generated by Django 3.1.3 on 2021-05-11 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='threatinitial',
            name='angle',
            field=models.IntegerField(default=0, max_length=10, null=True),
        ),
    ]
