# Generated by Django 5.0.3 on 2024-03-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=20)),
                ("age", models.PositiveIntegerField()),
                ("phone", models.PositiveIntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("aadhar", models.PositiveIntegerField()),
                ("street", models.CharField(max_length=30)),
                ("district", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("rating", models.IntegerField()),
                ("helper", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Helper",
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
                ("name", models.CharField(max_length=20)),
                ("age", models.PositiveIntegerField()),
                ("phone", models.PositiveIntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("aadhar", models.PositiveIntegerField()),
                ("street", models.CharField(max_length=30)),
                ("district", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("rating", models.IntegerField()),
                ("is_active", models.BooleanField(default=False)),
                ("skills", models.ManyToManyField(to="main.skill")),
            ],
        ),
    ]