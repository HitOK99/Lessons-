# Generated by Django 5.1.1 on 2024-11-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_work_window', '0024_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст коментаря')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
