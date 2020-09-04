from django.db import models
from django.urls import reverse


class PipeModel(models.Model):
    title = models.CharField('Название', max_length=120)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField(
        'Цена', default=0, max_digits=10, decimal_places=2)
    created = models.DateTimeField('Дата объявления', auto_now_add=True)
    is_active = models.BooleanField('Активен', default=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('pipe_detail',args=[self.pk])

    class Meta:
        verbose_name = 'Труба'
        verbose_name_plural = 'Трубы'


class PipeImageModel(models.Model):
    image = models.ImageField(
        'Изображение', upload_to='pipe_images/', default='default.jpg')
    pipe = models.ForeignKey(
        PipeModel, verbose_name='Труба', related_name='pipe_images', on_delete=models.CASCADE)
    is_main = models.BooleanField('Главное изображение', default=False)
    created = models.DateTimeField('Дата объявления', auto_now_add=True)
    is_active = models.BooleanField('Активен', default=True)

    def __str__(self):
        return f'{self.pipe}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
