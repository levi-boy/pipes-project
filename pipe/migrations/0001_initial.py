# Generated by Django 3.1.1 on 2020-09-03 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PipeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата объявления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Труба',
                'verbose_name_plural': 'Трубы',
            },
        ),
        migrations.CreateModel(
            name='PipeImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='pipe_images/', verbose_name='Изображение')),
                ('is_main', models.BooleanField(default=False, verbose_name='Главное изображение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата объявления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('pipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pipe.pipemodel', verbose_name='Труба')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]