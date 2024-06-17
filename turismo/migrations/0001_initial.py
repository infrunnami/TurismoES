# Generated by Django 5.0.6 on 2024-06-16 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foto', models.ImageField(upload_to='fotos/')),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
