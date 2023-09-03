from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    experience = models.CharField(max_length=250, unique=True)
    job_type = models.CharField(max_length=150)
    job_category = models.CharField(max_length=150)
    highest_education = models.CharField(max_length=150)
    job_description = models.CharField(max_length=150)
    profile_pic = models.ImageField(upload_to="app/img/candidate")
    class meta:
        managed = False


class Company(models.Model):
    client_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    about = models.CharField(max_length=1500)
    website = models.CharField(max_length=150)
    company_logo = models.ImageField(upload_to="app/img/company")

class JobDetails(models.Model):
    id = models.ForeignKey(Company,on_delete=models.CASCADE,primary_key=True,unique=True)
    jobname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    companyaddress = models.CharField(max_length=250)
    jobdescription = models.TextField(max_length=500)
    qualification = models.CharField(max_length=250)
    responsibilities = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    website = models.CharField(max_length=250)
    companyemail = models.CharField(max_length=50)
    companycontact = models.CharField(max_length=20)
    salarypackage = models.CharField(max_length=250)
    jobexperience = models.IntegerField(unique=True)
    companyimage = models.ImageField(upload_to="app/img/JobDetails",default=False)
    


    
