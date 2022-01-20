<<<<<<< HEAD
# Generated by Django 3.0.4 on 2021-12-23 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='photo')),
                ('comment', models.TextField(blank=True, max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('meow_count', models.IntegerField(default=0)),
                ('detail', models.BooleanField(blank=True, default=True)),
                ('gender', models.BooleanField(blank=True, default=True)),
                ('age', models.CharField(blank=True, max_length=30)),
                ('kind', models.CharField(blank=True, max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_owner', to=settings.AUTH_USER_MODEL, verbose_name='オーナー')),
            ],
            options={
                'db_table': 'posts',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Meow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meow_owner', to=settings.AUTH_USER_MODEL)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myposts.Post')),
            ],
        ),
    ]
=======
# Generated by Django 3.0.4 on 2021-12-23 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='photo')),
                ('comment', models.TextField(blank=True, max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('meow_count', models.IntegerField(default=0)),
                ('detail', models.BooleanField(blank=True, default=True)),
                ('gender', models.BooleanField(blank=True, default=True)),
                ('age', models.CharField(blank=True, max_length=30)),
                ('kind', models.CharField(blank=True, max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_owner', to=settings.AUTH_USER_MODEL, verbose_name='オーナー')),
            ],
            options={
                'db_table': 'posts',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Meow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meow_owner', to=settings.AUTH_USER_MODEL)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myposts.Post')),
            ],
        ),
    ]
>>>>>>> cf12ca6 (at my mac)
