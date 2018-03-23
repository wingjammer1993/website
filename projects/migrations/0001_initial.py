# Generated by Django 2.0.3 on 2018-03-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('institute', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
            ],
        ),
    ]
