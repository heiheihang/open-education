# Generated by Django 3.0.4 on 2020-03-28 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.IntegerField(default=0)),
                ('difficulty', models.IntegerField(default=0)),
                ('problem_text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(default=0)),
                ('student_name', models.CharField(max_length=30)),
                ('point', models.IntegerField(default=0)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mllearning.ClassGroup')),
            ],
        ),
    ]