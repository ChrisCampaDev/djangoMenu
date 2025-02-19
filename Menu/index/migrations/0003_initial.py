# Generated by Django 5.1.6 on 2025-02-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0002_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('gramaje', models.PositiveIntegerField(help_text='Peso en gramos')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('Lácteo', 'Lácteo'), ('Fruta', 'Fruta'), ('Verdura', 'Verdura'), ('Carne', 'Carne'), ('Bebida', 'Bebida'), ('Otro', 'Otro')], default='Otro', max_length=50)),
            ],
        ),
    ]
