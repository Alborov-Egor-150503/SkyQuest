from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0012_auto_20210710_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
