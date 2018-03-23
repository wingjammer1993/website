# Generated by Django 2.0.3 on 2018-03-23 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='education',
            name='to_date',
        ),
        migrations.AddField(
            model_name='education',
            name='year',
            field=models.CharField(default=django.utils.timezone.now, max_length=2000),
            preserve_default=False,
        ),
    ]
