# Generated by Django 3.0.3 on 2020-05-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('violations', '0002_auto_20200526_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='violation',
            old_name='Comment',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='person',
            name='violation',
        ),
        migrations.AlterField(
            model_name='violation',
            name='violatorFIO',
            field=models.CharField(max_length=100, verbose_name='ФИО нарушителя'),
        ),
    ]
