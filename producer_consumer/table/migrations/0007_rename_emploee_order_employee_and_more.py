# Generated by Django 4.2.4 on 2023-08-24 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0006_alter_order_emploee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='emploee',
            new_name='employee',
        ),
        migrations.AlterField(
            model_name='account',
            name='probation',
            field=models.BooleanField(default=False),
        ),
    ]
