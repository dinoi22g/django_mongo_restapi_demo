# Generated by Django 4.2.8 on 2023-12-27 17:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=20, verbose_name='標題')),
                ('content', models.TextField(verbose_name='內容')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='創建日期')),
            ],
        ),
    ]
