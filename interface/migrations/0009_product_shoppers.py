# Generated by Django 4.2.4 on 2023-12-09 14:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interface', '0008_blog_meta_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shoppers',
            field=models.ManyToManyField(blank=True, related_name='shopping_cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
