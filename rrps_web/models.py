from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class SixthClassAdmission(models.Model):
    dateofApp = models.DateTimeField(default=timezone.now)
    email_Id = models.EmailField(unique=True)
    Student_Photo = models.ImageField(upload_to='pics',blank=True)
    Student_Name = models.CharField(max_length = 150,blank=False)
    Surname= models.CharField(max_length = 150)
    Father_full_name = models.CharField(max_length = 150)
    Father_mobile_number = models.PositiveIntegerField(blank=True)


    Mother_Full_Name = models.CharField(max_length = 150)
    Mother_mobile_number = models.PositiveIntegerField(blank=True)
    Gaurdian_Name = models.CharField(max_length = 150,blank=True)
    Gaurdian_mobile_number = models.PositiveIntegerField(blank=True)
    Relation_with_Gaurdian = models.CharField(max_length = 150,blank=True)

    # Date_of_Birth = models.DateField()
    age = models.PositiveIntegerField()
    Nationality = models.CharField(max_length=200)
    Religion = models.CharField(max_length=100)
    Caste = models.CharField(max_length=6)
    Student_Aadhaar_number = models.PositiveIntegerField()
    Father_Aadhaar_number = models.PositiveIntegerField(blank=True)
    Mother_Aadhaar_number = models.PositiveIntegerField(blank=True)
    Rice_or_Ration_card_number = models.CharField(max_length = 150,blank=True)
    Whether_admitted_with_RS_or_TC =models.CharField(max_length=3,blank=True)
    Class_studied_previously = models.PositiveIntegerField()
    Previous_School = models.CharField(max_length=256)


    def get_absolute_url(self):
        return reverse('rrps_web:success')



    def __str__(self):

        return self.Student_Name + ' ' + self.email_Id

class SevenClassAdmission(models.Model):
    email_Id = models.EmailField(unique=True)
    Student_Photo = models.ImageField(blank=True)
    Student_Name = models.CharField(max_length = 150,blank=False)
    Surname= models.CharField(max_length = 150)
    Father_full_name = models.CharField(max_length = 150)
    Father_mobile_number = models.PositiveIntegerField(blank=True)


    Mother_Full_Name = models.CharField(max_length = 150)
    Mother_mobile_number = models.PositiveIntegerField(blank=True)
    Gaurdian_Name = models.CharField(max_length = 150,blank=True)
    Gaurdian_mobile_number = models.PositiveIntegerField(blank=True)
    Relation_with_Gaurdian = models.CharField(max_length = 150,blank=True)

    # Date_of_Birth = models.DateField()
    age = models.PositiveIntegerField()
    Nationality = models.CharField(max_length=200)
    Religion = models.CharField(max_length=100)
    Caste = models.CharField(max_length=6)
    Student_Aadhaar_number = models.PositiveIntegerField()
    Father_Aadhaar_number = models.PositiveIntegerField(blank=True)
    Mother_Aadhaar_number = models.PositiveIntegerField(blank=True)
    Rice_or_Ration_card_number = models.CharField(max_length = 150,blank=True)
    Whether_admitted_with_RS_or_TC =models.CharField(max_length=3,blank=True)
    Class_studied_previously = models.PositiveIntegerField()
    Previous_School = models.CharField(max_length=256)


    def get_absolute_url(self):
        return reverse('rrps_web:success')



    def __str__(self):

        return self.Student_Name

class EightClassAdmission(models.Model):
    email_Id = models.EmailField(unique=True)
    Student_Photo = models.ImageField(blank=True)
    Student_Name = models.CharField(max_length = 150,blank=False)
    Surname= models.CharField(max_length = 150)
    Father_full_name = models.CharField(max_length = 150)
    Father_mobile_number = models.PositiveIntegerField(blank=True)


    Mother_Full_Name = models.CharField(max_length = 150)
    Mother_mobile_number = models.PositiveIntegerField(blank=True)
    Gaurdian_Name = models.CharField(max_length = 150,blank=True)
    Gaurdian_mobile_number = models.PositiveIntegerField(blank=True)
    Relation_with_Gaurdian = models.CharField(max_length = 150,blank=True)

    # Date_of_Birth = models.DateField()
    age = models.PositiveIntegerField()
    Nationality = models.CharField(max_length=200)
    Religion = models.CharField(max_length=100)
    Caste = models.CharField(max_length=6)
    Student_Aadhaar_number = models.PositiveIntegerField()
    Father_Aadhaar_number = models.PositiveIntegerField(blank=True)
    Mother_Aadhaar_number = models.PositiveIntegerField(blank=True)
    Rice_or_Ration_card_number = models.CharField(max_length = 150,blank=True)
    Whether_admitted_with_RS_or_TC =models.CharField(max_length=3,blank=True)
    Class_studied_previously = models.PositiveIntegerField()
    Previous_School = models.CharField(max_length=256)


    def get_absolute_url(self):
        return reverse('rrps_web:success')



    def __str__(self):

        return self.Student_Name

class NinethClassAdmission(models.Model):
    email_Id = models.EmailField(unique=True)
    Student_Photo = models.ImageField(blank=True)
    Student_Name = models.CharField(max_length = 150,blank=False)
    Surname= models.CharField(max_length = 150)
    Father_full_name = models.CharField(max_length = 150)
    Father_mobile_number = models.PositiveIntegerField(blank=True)


    Mother_Full_Name = models.CharField(max_length = 150)
    Mother_mobile_number = models.PositiveIntegerField(blank=True)
    Gaurdian_Name = models.CharField(max_length = 150,blank=True)
    Gaurdian_mobile_number = models.PositiveIntegerField(blank=True)
    Relation_with_Gaurdian = models.CharField(max_length = 150,blank=True)

    # Date_of_Birth = models.DateField()
    age = models.PositiveIntegerField()
    Nationality = models.CharField(max_length=200)
    Religion = models.CharField(max_length=100)
    Caste = models.CharField(max_length=6)
    Student_Aadhaar_number = models.PositiveIntegerField()
    Father_Aadhaar_number = models.PositiveIntegerField(blank=True)
    Mother_Aadhaar_number = models.PositiveIntegerField(blank=True)
    Rice_or_Ration_card_number = models.CharField(max_length = 150,blank=True)
    Whether_admitted_with_RS_or_TC =models.CharField(max_length=3,blank=True)
    Class_studied_previously = models.PositiveIntegerField()
    Previous_School = models.CharField(max_length=256)


    def get_absolute_url(self):
        return reverse('rrps_web:success')



    def __str__(self):

        return self.Student_Name

class TenthClassAdmission(models.Model):
    email_Id = models.EmailField(unique=True)
    Student_Photo = models.ImageField(blank=True)
    Student_Name = models.CharField(max_length = 150,blank=False)
    Surname= models.CharField(max_length = 150)
    Father_full_name = models.CharField(max_length = 150)
    Father_mobile_number = models.PositiveIntegerField(blank=True)


    Mother_Full_Name = models.CharField(max_length = 150)
    Mother_mobile_number = models.PositiveIntegerField(blank=True)
    Gaurdian_Name = models.CharField(max_length = 150,blank=True)
    Gaurdian_mobile_number = models.PositiveIntegerField(blank=True)
    Relation_with_Gaurdian = models.CharField(max_length = 150,blank=True)

    # Date_of_Birth = models.DateField()
    age = models.PositiveIntegerField()
    Nationality = models.CharField(max_length=200)
    Religion = models.CharField(max_length=100)
    Caste = models.CharField(max_length=6)
    Student_Aadhaar_number = models.PositiveIntegerField()
    Father_Aadhaar_number = models.PositiveIntegerField(blank=True)
    Mother_Aadhaar_number = models.PositiveIntegerField(blank=True)
    Rice_or_Ration_card_number = models.CharField(max_length = 150,blank=True)
    Whether_admitted_with_RS_or_TC =models.CharField(max_length=3,blank=True)
    Class_studied_previously = models.PositiveIntegerField()
    Previous_School = models.CharField(max_length=256)


    def get_absolute_url(self):
        return reverse('rrps_web:success')



    def __str__(self):

        return self.Student_Name

class Announcement(models.Model):

    Description = models.CharField(max_length=500)
    dateofan =models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Description
