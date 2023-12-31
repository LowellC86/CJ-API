# Generated by Django 4.2.3 on 2023-07-26 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo_url', models.TextField()),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no title', max_length=100)),
                ('image_url', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(default='')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stickers', to='cjmonet.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no title', max_length=100)),
                ('preview_url', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(default='')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paintings', to='cjmonet.artist')),
            ],
        ),
    ]
