# Generated by Django 2.1.3 on 2018-12-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makers_home_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscription_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usermembership',
            name='phone_number',
            field=models.CharField(max_length=14),
        ),
    ]