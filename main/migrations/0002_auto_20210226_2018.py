# Generated by Django 3.1 on 2021-02-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='recipes',
            new_name='recipe',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
