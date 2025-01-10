# Generated by Django 5.1.4 on 2025-01-10 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Catégories',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name'], 'verbose_name_plural': 'Auteurs'},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['title'], 'verbose_name_plural': 'Livres'},
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.category'),
        ),
    ]
