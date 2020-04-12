# Generated by Django 3.0.4 on 2020-04-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mllearning', '0002_classgroup_class_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classgroup',
            name='id',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='classgroup',
            name='class_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
