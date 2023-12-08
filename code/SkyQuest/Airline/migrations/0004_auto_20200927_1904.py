from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0003_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdetail',
            name='NumberOfTraveller',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
