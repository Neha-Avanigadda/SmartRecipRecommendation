# Generated by Django 5.0.7 on 2024-12-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('youtube_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
