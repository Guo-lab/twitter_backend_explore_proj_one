# Generated by Django 3.1.3 on 2023-03-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='type',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
