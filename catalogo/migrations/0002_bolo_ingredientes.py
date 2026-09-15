from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolo',
            name='ingredientes',
            field=models.TextField(default=''),
        ),
    ]
