# Generated by Django 5.1.5 on 2025-04-24 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_fp', '0035_remove_actor_film_alter_item_actors'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
