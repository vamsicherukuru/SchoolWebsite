# Generated by Django 3.0.3 on 2020-05-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrps_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EightClassAdmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_Id', models.EmailField(max_length=254, unique=True)),
                ('Student_Photo', models.ImageField(blank=True, upload_to='')),
                ('Student_Name', models.CharField(max_length=150)),
                ('Surname', models.CharField(max_length=150)),
                ('Father_full_name', models.CharField(max_length=150)),
                ('Father_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Mother_Full_Name', models.CharField(max_length=150)),
                ('Mother_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Gaurdian_Name', models.CharField(blank=True, max_length=150)),
                ('Gaurdian_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Relation_with_Gaurdian', models.CharField(blank=True, max_length=150)),
                ('age', models.PositiveIntegerField()),
                ('Nationality', models.CharField(max_length=200)),
                ('Religion', models.CharField(max_length=100)),
                ('Caste', models.CharField(max_length=6)),
                ('Student_Aadhaar_number', models.PositiveIntegerField()),
                ('Father_Aadhaar_number', models.PositiveIntegerField(blank=True)),
                ('Mother_Aadhaar_number', models.PositiveIntegerField(blank=True)),
                ('Rice_or_Ration_card_number', models.CharField(blank=True, max_length=150)),
                ('Whether_admitted_with_RS_or_TC', models.CharField(blank=True, max_length=3)),
                ('Class_studied_previously', models.PositiveIntegerField()),
                ('Previous_School', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='NinethClassAdmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_Id', models.EmailField(max_length=254, unique=True)),
                ('Student_Photo', models.ImageField(blank=True, upload_to='')),
                ('Student_Name', models.CharField(max_length=150)),
                ('Surname', models.CharField(max_length=150)),
                ('Father_full_name', models.CharField(max_length=150)),
                ('Father_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Mother_Full_Name', models.CharField(max_length=150)),
                ('Mother_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Gaurdian_Name', models.CharField(blank=True, max_length=150)),
                ('Gaurdian_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Relation_with_Gaurdian', models.CharField(blank=True, max_length=150)),
                ('age', models.PositiveIntegerField()),
                ('Nationality', models.CharField(max_length=200)),
                ('Religion', models.CharField(max_length=100)),
                ('Caste', models.CharField(max_length=6)),
                ('Student_Aadhaar_number', models.PositiveIntegerField()),
                ('Father_Aadhaar_number', models.PositiveIntegerField(blank=True)),
                ('Mother_Aadhaar_number', models.PositiveIntegerField(blank=True)),
                ('Rice_or_Ration_card_number', models.CharField(blank=True, max_length=150)),
                ('Whether_admitted_with_RS_or_TC', models.CharField(blank=True, max_length=3)),
                ('Class_studied_previously', models.PositiveIntegerField()),
                ('Previous_School', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SevenClassAdmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_Id', models.EmailField(max_length=254, unique=True)),
                ('Student_Photo', models.ImageField(blank=True, upload_to='')),
                ('Student_Name', models.CharField(max_length=150)),
                ('Surname', models.CharField(max_length=150)),
                ('Father_full_name', models.CharField(max_length=150)),
                ('Father_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Mother_Full_Name', models.CharField(max_length=150)),
                ('Mother_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Gaurdian_Name', models.CharField(blank=True, max_length=150)),
                ('Gaurdian_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Relation_with_Gaurdian', models.CharField(blank=True, max_length=150)),
                ('age', models.PositiveIntegerField()),
                ('Nationality', models.CharField(max_length=200)),
                ('Religion', models.CharField(max_length=100)),
                ('Caste', models.CharField(max_length=6)),
                ('Student_Aadhaar_number', models.PositiveIntegerField()),
                ('Father_Aadhaar_number', models.PositiveIntegerField(blank=True)),
                ('Mother_Aadhaar_number', models.PositiveIntegerField(blank=True)),
                ('Rice_or_Ration_card_number', models.CharField(blank=True, max_length=150)),
                ('Whether_admitted_with_RS_or_TC', models.CharField(blank=True, max_length=3)),
                ('Class_studied_previously', models.PositiveIntegerField()),
                ('Previous_School', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SixthClassAdmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_Id', models.EmailField(max_length=254, unique=True)),
                ('Student_Photo', models.ImageField(blank=True, upload_to='')),
                ('Student_Name', models.CharField(max_length=150)),
                ('Surname', models.CharField(max_length=150)),
                ('Father_full_name', models.CharField(max_length=150)),
                ('Father_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Mother_Full_Name', models.CharField(max_length=150)),
                ('Mother_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Gaurdian_Name', models.CharField(blank=True, max_length=150)),
                ('Gaurdian_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Relation_with_Gaurdian', models.CharField(blank=True, max_length=150)),
                ('age', models.PositiveIntegerField()),
                ('Nationality', models.CharField(max_length=200)),
                ('Religion', models.CharField(max_length=100)),
                ('Caste', models.CharField(max_length=6)),
                ('Student_Aadhaar_number', models.PositiveIntegerField()),
                ('Father_Aadhaar_number', models.PositiveIntegerField(blank=True)),
                ('Mother_Aadhaar_number', models.PositiveIntegerField(blank=True)),
                ('Rice_or_Ration_card_number', models.CharField(blank=True, max_length=150)),
                ('Whether_admitted_with_RS_or_TC', models.CharField(blank=True, max_length=3)),
                ('Class_studied_previously', models.PositiveIntegerField()),
                ('Previous_School', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TenthClassAdmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_Id', models.EmailField(max_length=254, unique=True)),
                ('Student_Photo', models.ImageField(blank=True, upload_to='')),
                ('Student_Name', models.CharField(max_length=150)),
                ('Surname', models.CharField(max_length=150)),
                ('Father_full_name', models.CharField(max_length=150)),
                ('Father_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Mother_Full_Name', models.CharField(max_length=150)),
                ('Mother_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Gaurdian_Name', models.CharField(blank=True, max_length=150)),
                ('Gaurdian_mobile_number', models.PositiveIntegerField(blank=True)),
                ('Relation_with_Gaurdian', models.CharField(blank=True, max_length=150)),
                ('age', models.PositiveIntegerField()),
                ('Nationality', models.CharField(max_length=200)),
                ('Religion', models.CharField(max_length=100)),
                ('Caste', models.CharField(max_length=6)),
                ('Student_Aadhaar_number', models.PositiveIntegerField()),
                ('Father_Aadhaar_number', models.PositiveIntegerField(blank=True)),
                ('Mother_Aadhaar_number', models.PositiveIntegerField(blank=True)),
                ('Rice_or_Ration_card_number', models.CharField(blank=True, max_length=150)),
                ('Whether_admitted_with_RS_or_TC', models.CharField(blank=True, max_length=3)),
                ('Class_studied_previously', models.PositiveIntegerField()),
                ('Previous_School', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='Student_Photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
