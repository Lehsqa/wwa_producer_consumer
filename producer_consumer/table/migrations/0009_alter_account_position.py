# Generated by Django 4.2.4 on 2023-08-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0008_alter_account_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='position',
            field=models.CharField(default='Developer', max_length=100),
        ),
    ]
