import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(
                    max_length=255,
                    verbose_name='Имя',
                )),
                ('position', models.CharField(
                    max_length=255,
                    verbose_name='Должность',
                )),
                ('city', models.CharField(
                    max_length=255,
                    verbose_name='Город',
                )),
                ('is_admin', models.BooleanField(
                    default=False,
                )),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                )),
                ('name', models.CharField(
                    max_length=255,
                    verbose_name='Название',
                )),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='AccountTask',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                )),
                ('checking', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='checking',
                    to='todo.Account',
                    verbose_name='Ответственный',
                )),
                ('performer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='performers',
                    to='todo.Account',
                    verbose_name='Исполняющий',
                )),
                ('task', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='todo.Task',
                )),
            ],
        ),
    ]
