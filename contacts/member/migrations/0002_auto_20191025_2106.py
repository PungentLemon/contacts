# Generated by Django 2.2.6 on 2019-10-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(upload_to='pictures/%y/%m/%d/'),
        ),
    ]
