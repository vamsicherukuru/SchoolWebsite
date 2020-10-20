# Generated by Django 3.0.3 on 2020-05-25 16:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rrps_web', '0002_auto_20200524_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=500)),
                ('dateofan', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='StudentDetails',
        ),
        migrations.AlterField(
            model_name='sixthclassadmission',
            name='Student_Photo',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
