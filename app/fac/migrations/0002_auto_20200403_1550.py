# Generated by Django 2.2.11 on 2020-04-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='apeliidos',
            new_name='apellidos',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Natural', 'Natural'), ('Juridica', 'Juridica')], default='Natural', max_length=10),
        ),
    ]