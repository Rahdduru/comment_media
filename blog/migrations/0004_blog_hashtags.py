# Generated by Django 2.2.1 on 2019-06-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='blog.Hashtag'),
        ),
    ]