# Generated by Django 4.2 on 2023-04-13 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliweb', '0004_remove_about_picture_alter_comment_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='portfoliweb/templates/portfoliweb/assets/images'),
        ),
    ]