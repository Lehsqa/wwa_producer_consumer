# Generated by Django 4.2.4 on 2023-08-24 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0010_alter_account_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='position',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
