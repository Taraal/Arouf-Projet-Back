# Generated by Django 3.0 on 2019-12-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0002_auto_20191203_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
