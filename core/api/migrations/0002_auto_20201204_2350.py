# Generated by Django 3.1.4 on 2020-12-04 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.education'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='experience',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.experience'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.social'),
        ),
    ]
