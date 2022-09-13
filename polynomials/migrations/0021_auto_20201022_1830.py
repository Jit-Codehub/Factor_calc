# Generated by Django 3.0.7 on 2020-10-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polynomials', '0020_poly_root_db'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fact_poly_db',
            options={},
        ),
        migrations.AlterField(
            model_name='fact_poly_db',
            name='date_modified',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='fact_poly_db',
            name='finalAnswer',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='fact_poly_db',
            name='inputEnter',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='fact_poly_db',
            name='slug',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='fact_poly_db',
            name='solutionTitle',
            field=models.TextField(max_length=250),
        ),
    ]
