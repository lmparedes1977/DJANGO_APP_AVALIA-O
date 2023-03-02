# Generated by Django 4.1.7 on 2023-03-02 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Aplicativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('descricao', models.TextField()),
                ('slug', models.SlugField()),
                ('ano_lancamento', models.IntegerField()),
                ('nr_usuarios', models.IntegerField()),
                ('foto', models.ImageField(upload_to='imagens/%Y/%m/%d/')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='python.categoria')),
            ],
        ),
    ]