from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0008_auto_20200930_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdetail',
            name='Duration',
            field=models.DurationField(),
        ),
    ]
