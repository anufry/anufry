# Generated by Django 2.2.20 on 2021-04-08 09:58

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=128, verbose_name='URL-компонент')),
                ('text', martor.models.MartorField(verbose_name='Текст')),
                ('meta_keywords', models.CharField(blank=True, help_text='Укажите слова или фразы через запятую', max_length=1024, null=True, verbose_name='Мета-ключевые слова')),
                ('meta_description', models.CharField(blank=True, help_text='Укажите несколько строк краткого описания', max_length=1024, null=True, verbose_name='Meta-описание')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]