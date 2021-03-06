# Generated by Django 3.1.1 on 2020-10-17 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='comments.node')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post'),
        ),
        migrations.CreateModel(
            name='NodeClosure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth', models.IntegerField()),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodeclosure_parents', to='comments.node')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodeclosure_children', to='comments.node')),
            ],
            options={
                'db_table': 'comments_nodeclosure',
                'unique_together': {('parent', 'child')},
            },
        ),
    ]
