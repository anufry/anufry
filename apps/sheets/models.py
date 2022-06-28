from django.db import models
# from ckeditor.fields import RichTextField
from martor.models import MartorField

class Sheet(models.Model):
    
    title = models.CharField('Заголовок', max_length=128)
    slug = models.SlugField('URL-компонент', max_length=128, )
    text = MartorField('Текст',)
    meta_keywords = models.CharField('Мета-ключевые слова', max_length=1024, null=True, blank=True, help_text='Укажите слова или фразы через запятую',)
    meta_description = models.CharField('Meta-описание', max_length=1024, null=True, blank=True, help_text='Укажите несколько строк краткого описания',)


    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.title

