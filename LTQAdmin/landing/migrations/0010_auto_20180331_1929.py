# Generated by Django 2.0.3 on 2018-03-31 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_auto_20180331_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='level_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='landing.Level'),
        ),
    ]
