# Generated by Django 2.2.1 on 2019-06-04 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image',
            new_name='images',
        ),
    ]
