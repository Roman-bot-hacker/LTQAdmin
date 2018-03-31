# Generated by Django 2.0.3 on 2018-03-31 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_auto_20180331_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='level_id',
            field=models.ForeignKey(choices=[('1', 'Level 1'), ('2', 'Level 2'), ('3', 'Level 3')], on_delete=django.db.models.deletion.CASCADE, to='landing.Level'),
        ),
    ]
