# Generated by Django 5.0.1 on 2024-02-02 18:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_alter_empresa_usuarios_projeto_empresa_projetos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='usuario',
        ),
        migrations.AddField(
            model_name='projeto',
            name='usuario',
            field=models.ManyToManyField(related_name='projetos', to=settings.AUTH_USER_MODEL),
        ),
    ]
