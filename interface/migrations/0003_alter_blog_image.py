# Generated by Django 4.2.4 on 2023-12-05 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0002_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
