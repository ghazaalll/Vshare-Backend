# Generated by Django 3.1.7 on 2021-05-31 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='have_notice',
            field=models.BooleanField(default=False),
        ),
    ]
