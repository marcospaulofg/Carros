# Generated by Django 5.2 on 2025-04-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Carros",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("modelo", models.CharField(max_length=50)),
                ("marca", models.CharField(max_length=50)),
                ("ano", models.IntegerField(blank=True, null=True)),
                ("km", models.IntegerField(blank=True, null=True)),
                ("cor", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "preco",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
            ],
        ),
    ]
