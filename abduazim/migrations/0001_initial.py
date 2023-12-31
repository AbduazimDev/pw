# Generated by Django 4.2 on 2023-06-14 04:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='.')),
                ('title', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('birthday', models.DateField()),
                ('location', models.CharField(max_length=250)),
                ('about_me', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=500)),
                ('blog', ckeditor.fields.RichTextField()),
                ('shortblog', models.CharField(max_length=250)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='.')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ClientLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='.')),
                ('url', models.CharField(blank=True, default='#', max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('picture', models.ImageField(upload_to='.')),
                ('comentary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experince',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=250)),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('picture', models.FileField(upload_to='.')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('lavel', models.IntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('picture', models.ImageField(upload_to='.')),
                ('link', models.CharField(blank=True, default='#', max_length=250, null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('date', models.DateField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abduazim.category')),
            ],
        ),
    ]
