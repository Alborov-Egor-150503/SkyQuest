from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlightDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AirlineName', models.CharField(max_length=30)),
                ('DepartureTime', models.DateTimeField()),
                ('ArrivalTime', models.DateTimeField()),
                ('NumberOfTraveller', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Duration', models.TimeField(null=True)),
                ('AvailableSeat', models.IntegerField(null=True)),
                ('FromLocation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='From', to='Airline.place')),
                ('ToLocation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='To', to='Airline.place')),
            ],
        ),
    ]
