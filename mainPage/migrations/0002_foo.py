# Generated by Django 3.0.3 on 2020-03-27 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_private', models.BooleanField(default=False)),
            ],
        ),
    ]