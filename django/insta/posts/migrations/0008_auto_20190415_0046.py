# Generated by Django 2.1.8 on 2019-04-15 00:46

from django.db import migrations
import imagekit.models.fields
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20190415_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=imagekit.models.fields.ProcessedImageField(upload_to=posts.models.post_image_path),
        ),
    ]
