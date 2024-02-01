# Generated by Django 5.0 on 2023-12-26 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeNest', '0012_alter_course_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCourse',
            fields=[
                ('Mid', models.AutoField(primary_key=True, serialize=False)),
                ('Mname', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KnowledgeNest.maincourse'),
        ),
    ]