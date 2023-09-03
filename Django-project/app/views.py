from django.shortcuts import render,redirect
from .models import *
import random
from django.contrib.sessions.middleware import SessionMiddleware


# Create your views here.

def IndexPage(request):
    return  render(request,"app/index.html")

def SignPage(request):
    
     return render(request,"app/signup.html")

def CSignPage(request):
    
    return render(request,"app/signup2.html")



def RegisterUser(request):
    if request.method == "POST":
        global role
        role = "Candidate"
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)
        if user:
            message = "User already Exists!"
            return render(request,"app/signup.html",{'msg': message})
        else:
            if password == cpassword:
                otp = random.randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
    else:
        print("Company Registration")
def RegisterClient(request):
    if request.method == "POST":
        global role
        role = "Company"
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        client = UserMaster.objects.filter(email=email)
        if client:
            message = "Client already Exists"
            return render(request,"app/signup2.html",{'msg':message})
        else:
            if password == cpassword:
                otp= random.randint(100000,999999)
                newclient = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcomp = Company.objects.create(client_id=newclient,firstname=fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
    else:
        print("Candidate Registration")

def Login(request):
    return render(request,"app/login.html")

def Otpverify(request):
    return render(request,"app/otpverify.html")

def OtpVerification(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)

    if user:
        if user.otp == otp:
            message = "Otp Verification Successful!"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "Otp Verification failed"
            return render(request,"app/otpverify.html",{'msg':message})
        
    else:
        return render(request,"app/signup.html")

def LoginPage(request):
    return render(request,"app/login.html")

def LoginUser(request):
    global role
    role = "Candidate"
    role = "Company"
    if request.POST['role'] == "Candidate":
        email = request.POST['email']
        password = request.POST['password']
        
        user = UserMaster.objects.get(email=email)
        if user:
            if user.password == password and user.role=="Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password
                return render(request,"app/homepage.html")
            else:
                message = "Password Does Not Match!"
                return render(request,"app/login.html",{'msg':message})

            
        else:
            message = "User does not exist"
            return render(request,"app/login.html",{'msg':message})

    if request.POST['role'] == "Company":
        email = request.POST['email']
        password = request.POST['password']

        client = UserMaster.objects.get(email=email)
        if client:
            if client.password == password and client.role == "Company":
                comp = Company.objects.get(client_id=client)
                request.session['id'] = client.id
                request.session['role'] = client.role
                request.session['firstname'] = comp.firstname
                request.session['lastname'] = comp.lastname
                request.session['email'] = client.email
                request.session['password'] = client.password
                return redirect('companyindex')
            else:
                message = "Password do not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "Client does not exist"
            return render(request,"app/login.html",{'msg':message})


def ProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)
    return render(request,"app/profile.html",{'user':user,'can':can})

def ProfilePagec(request,pk):
    client = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(client_id=client)
    return render(request,"app/profilec.html",{'client':client,'comp':comp})

def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.contact = request.POST['contact']
        can.state = request.POST['state']
        can.city = request.POST['city']
        can.address = request.POST['address']
        can.dob = request.POST['dob']
        can.gender = request.POST['gender']
        can.experience = request.POST['experience']
        can.job_type = request.POST['jobtype']
        can.job_category = request.POST['jobcategory']
        can.highest_education = request.POST['highesteducation']
        can.job_description = request.POST['jobdescription']
        can.save()
        url = f'/profile/{pk}' #formatting URL
        return redirect(url)
def UpdateProfilec(request,pk):
    client = UserMaster.objects.get(pk=pk)
    if client.role == "Company":
        comp = Company.objects.get(client_id=client)
        comp.company_name = request.POST['companyname']
        comp.state = request.POST['state']
        comp.city = request.POST['city']
        comp.contact = request.POST['contact']
        comp.address = request.POST['address']
        comp.about = request.POST['about']
        comp.website = request.POST['website']
        comp.save()
        url = f'/profilec/{pk}'
        return redirect(url)
# company side
def CompanyIndexPage(request):
    return render(request,"app/company/index.html")

def JobPostPage(request):
    return render(request,"app/company/jobpost.html")

def JobDetailSubmit(request,id):
     
    
     
    client = UserMaster.objects.get(id=id)
    
   
    if client.role == "Company":
        comp = Company.objects.get(client_id=client)
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        companyemail = request.POST['companyemail']
        companycontact = request.POST['companycontact']
        companyaddress = request.POST['companyaddress']
        jobdescription = request.POST['jobdescription']
        qualification = request.POST['qualification']
        responsibilities = request.POST['responsibilities']
        location = request.POST['location']
        salarypackage = request.POST['salarypackage']
        jobexperience = request.POST['jobexperience']
        website = request.POST['website']
        companyimage = request.FILES['companyimage']

        newjob = JobDetails.objects.create(id=comp,jobname=jobname,companyname=companyname,companyaddress=companyaddress,
        jobdescription=jobdescription,qualification=qualification,responsibilities=responsibilities,location=location,
        website=website,companyemail=companyemail,companycontact=companycontact,salarypackage=salarypackage,jobexperience=jobexperience,
        companyimage=companyimage)

        message = "Job Post Successfuly"
        return render(request,"app/company/jobpost.html",{'msg':message})
def TableView(request):
    return render(request,"app/company/tables.html")

def JobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/company/jobpostlist.html",{'all_job':all_job})

def CandidateJobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/job-listing.html",{'all_job':all_job})

def CompanyLogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')

def CandidateLogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')

def DetailsPage(request,id):
   
    all_job = JobDetails.objects.all()
    return render(request,"app/job-details.html",{'all_job':all_job})

def ApplyPage(request):
    return render(request,"app/apply.html")

        




