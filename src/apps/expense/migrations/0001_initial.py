# Generated by Django 5.0.2 on 2024-02-07 09:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("category", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Expense",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "categories",
                    models.ManyToManyField(
                        blank=True, related_name="expenses", to="category.category"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="expenses",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
