# Generated by Django 4.2.16 on 2024-10-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_faqtype_title_en_faqtype_title_ru_faqtype_title_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feadback',
            name='profession_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feadback',
            name='profession_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feadback',
            name='profession_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workers',
            name='full_name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workers',
            name='full_name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workers',
            name='full_name_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workers',
            name='profession_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workers',
            name='profession_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workers',
            name='profession_uz',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
