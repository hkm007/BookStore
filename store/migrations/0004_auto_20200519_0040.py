# Generated by Django 2.2.5 on 2020-05-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200519_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_category',
            field=models.CharField(choices=[('Technical', 'Technical'), ('Story', 'Story')], max_length=30),
        ),
    ]