# Generated by Django 3.1.7 on 2021-05-31 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_have_notice'),
        ('notifications', '0003_auto_20210531_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_from_group', to='groups.group', to_field='groupid'),
        ),
    ]
