# Generated by Django 3.1.1 on 2020-10-05 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comments.comment')),
                ('title', models.CharField(max_length=150, verbose_name='Название поста')),
                ('slug', models.SlugField(max_length=150, verbose_name='Слаг поста')),
                ('body', models.TextField(blank=True, verbose_name='Описание поста')),
                ('date_pub', models.DateTimeField(auto_now_add=True, verbose_name='Время создания поста')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('comments.comment',),
        ),
    ]