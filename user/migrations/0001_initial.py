# Generated by Django 4.1.7 on 2023-03-26 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserRounds",
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
                ("registered_round_one", models.BooleanField(default=False)),
                ("selected_round_two", models.BooleanField(default=False)),
                ("registered_round_two", models.BooleanField(default=False)),
                ("selected_round_three", models.BooleanField(default=False)),
                ("registered_round_three", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rounds",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserDetails",
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
                ("name", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("mobile", models.CharField(max_length=10)),
                ("college", models.CharField(max_length=50)),
                ("roll_number", models.CharField(max_length=25)),
                ("tricity_resident", models.BooleanField(default=True)),
                ("need_stay", models.BooleanField(default=False)),
                ("image_url", models.URLField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="details",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]