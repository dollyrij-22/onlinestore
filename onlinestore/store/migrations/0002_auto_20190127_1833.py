# Generated by Django 2.0.6 on 2019-01-27 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Customer'),
        ),
    ]