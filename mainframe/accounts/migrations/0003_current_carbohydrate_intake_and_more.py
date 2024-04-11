# Generated by Django 5.0 on 2024-02-22 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_current_name_remove_current_offer_current_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='current',
            name='carbohydrate_intake',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='current',
            name='existing_allergens',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='current',
            name='fats_intake',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='current',
            name='protein_intake',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='current',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='current',
            name='dietary_preference',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='current',
            name='existing_health_condition',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='current',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='current',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='current',
            name='lifestyle_preference',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='current',
            name='meal_portion_size',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='current',
            name='meals_per_day',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='current',
            name='physical_activity_level',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='current',
            name='weight',
            field=models.FloatField(),
        ),
    ]
