# Generated by Django 2.2.20 on 2021-04-08 08:10

from django.db import migrations, models
import django.utils.timezone
import martor.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('slug', models.SlugField(max_length=128, verbose_name='URL-компонент')),
                ('image', models.ImageField(upload_to='blog/teasers/', verbose_name='Бесполезное изображение')),
                ('teaser', martor.models.MartorField()),
                ('text', martor.models.MartorField()),
                ('posted_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата поста')),
                ('meta_keywords', models.CharField(blank=True, help_text='Для страницы со списком элементов категории. Укажите слова или фразы через запятую', max_length=1024, null=True, verbose_name='Мета-ключевые слова')),
                ('meta_description', models.CharField(blank=True, help_text='Для страницы со списком элементов категории. Укажите несколько строк краткого описания', max_length=1024, null=True, verbose_name='Meta-описание')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-posted_at'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['slug'], name='blog_post_slug_cdb902_idx'),
        ),
    ]
