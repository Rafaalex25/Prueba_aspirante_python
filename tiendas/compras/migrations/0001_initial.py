# Generated by Django 2.2.19 on 2021-05-30 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro_comercial', models.IntegerField(default=1)),
                ('distancia_comercial', models.IntegerField(default=10)),
                ('centro_comercial_visitado', models.IntegerField(default=1)),
            ],
        ),
    ]