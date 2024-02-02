# Generated by Django 5.0.1 on 2024-02-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('usuarios', models.ManyToManyField(related_name='empresas', to='usuarios.usuario')),
            ],
        ),
    ]