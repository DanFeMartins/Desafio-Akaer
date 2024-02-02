# Generated by Django 5.0.1 on 2024-02-02 14:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0006_remove_usuario_empresas_remove_usuario_usuario_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('usuarios', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
