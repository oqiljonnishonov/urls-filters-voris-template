# Generated by Django 4.1.3 on 2022-11-16 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangoapp", "0002_news_views"),
    ]

    operations = [
        migrations.CreateModel(
            name="Counts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.CharField(max_length=150, verbose_name="Categoriya"),
                ),
                (
                    "counts",
                    models.IntegerField(max_length=10, verbose_name="contentlar soni"),
                ),
            ],
            options={
                "verbose_name": "Kategoriya counter",
                "verbose_name_plural": "Kategoriyalar counters",
            },
        ),
    ]