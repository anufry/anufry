from django.db import models
from django.utils import timezone

from martor.models import MartorField
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.CharField('Название', max_length=128)
    slug = models.SlugField('URL-компонент', max_length=128,)
    image = models.ImageField('Бесполезное изображение', upload_to='blog/teasers/', help_text="Изображение 1200х300 (4х1)")
    teaser = MartorField('Короткое описания')
    text = MartorField('Полный текст')
    tags = TaggableManager('Теги')
    posted_at = models.DateField('Дата поста', default=timezone.now)

    meta_keywords = models.CharField('Мета-ключевые слова', max_length=1024, null=True, blank=True, help_text='Для страницы со списком элементов категории. Укажите слова или фразы через запятую',)
    meta_description = models.CharField('Meta-описание', max_length=1024, null=True, blank=True, help_text='Для страницы со списком элементов категории. Укажите несколько строк краткого описания',)


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-posted_at']
        indexes = [
            models.Index(fields=['slug',]),
        ] 
        

    def __str__(self):
        return f'{self.title}'