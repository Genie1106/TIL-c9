# Generated by Django 2.1.5 on 2019-01-31 02:44

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190131_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='posts/images'),
        ),
    ]
