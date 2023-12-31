import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0002_passenger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('phone', models.CharField(blank=True, default='', max_length=50)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Airline.flightdetail')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Airline.passenger')),
            ],
        ),
    ]
