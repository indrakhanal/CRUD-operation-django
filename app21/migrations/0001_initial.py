# Generated by Django 2.2.6 on 2020-02-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, default='', max_length=100)),
                ('mobile', models.CharField(blank=True, default='', max_length=100)),
                ('email', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ['fullname'],
            },
        ),
    ]
