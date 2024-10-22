# Generated by Django 2.2.5 on 2020-05-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200519_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_category',
            field=models.CharField(choices=[('Technical', 'Technical'), ('Story', 'Story')], max_length=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_class',
            field=models.CharField(choices=[('Premium', 'Premium'), ('Old', 'Old')], max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.CharField(choices=[('old', 'old'), ('new', 'new')], max_length=30),
        ),
    ]
