# Generated by Django 4.0.6 on 2022-07-31 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0039_branchdirectorie_product_entitydiretorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitydiretorie',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
