# Generated by Django 2.0.6 on 2019-01-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190127_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='staus',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.DateTimeField(null=True),
        ),
    ]