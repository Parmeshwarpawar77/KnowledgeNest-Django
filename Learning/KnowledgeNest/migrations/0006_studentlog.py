# Generated by Django 4.2.7 on 2023-12-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeNest', '0005_delete_studentlog_remove_student_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentlog',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
