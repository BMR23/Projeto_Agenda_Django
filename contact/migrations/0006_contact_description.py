# Generated by Django 4.2.3 on 2023-07-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_contact_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.TextField(default='Descrição', max_length=300),
        ),
    ]