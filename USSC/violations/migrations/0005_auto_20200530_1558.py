# Generated by Django 3.0.3 on 2020-05-30 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('violations', '0004_auto_20200529_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название объекта')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название профессии')),
            ],
        ),
        migrations.CreateModel(
            name='ViolationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование типа нарушения')),
            ],
        ),
        migrations.AlterField(
            model_name='violation',
            name='object_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='violations.Object'),
        ),
        migrations.AlterField(
            model_name='violation',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='violations.ViolationType'),
        ),
        migrations.AlterField(
            model_name='violation',
            name='violator_profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='violations.Profession'),
        ),
    ]
