# Generated by Django 4.0.6 on 2022-07-31 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0029_countersdirectorie_delete_counter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entitydiretorie',
            name='branchID',
        ),
        migrations.AddField(
            model_name='branchdirectorie',
            name='branchID',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
