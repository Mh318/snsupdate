<<<<<<< HEAD
# Generated by Django 3.0.4 on 2022-01-07 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myposts', '0007_auto_20220107_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/', verbose_name='アイコン画像'),
        ),
    ]
=======
# Generated by Django 3.0.4 on 2022-01-07 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myposts', '0007_auto_20220107_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/', verbose_name='アイコン画像'),
        ),
    ]
>>>>>>> cf12ca6 (at my mac)
