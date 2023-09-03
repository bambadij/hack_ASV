from django.urls import path,include
from . import views
from django.http import HttpResponse

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("signup/",views.SignPage,name="signup"),
    path("csignup/",views.CSignPage,name="csignup"),
    path("register/",views.RegisterUser,name="register"),
    path("cregister/",views.RegisterClient,name="cregister"),
    path("login/",views.Login,name="login"),
    path("otpverify/",views.Otpverify,name="otp"),
    path("otp/",views.OtpVerification,name="otpverify"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("homepage/",views.LoginUser,name="login"),
    path("profile/<int:pk>",views.ProfilePage,name="profile"),
    path("profilec/<int:pk>",views.ProfilePagec,name="profilec"),
    path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
    path("updateprofilec/<int:pk>",views.UpdateProfilec,name="updateprofilec"),
    #company
    path("companyindex/",views.CompanyIndexPage,name="companyindex"),
    path("jobpostpage/",views.JobPostPage,name="jobpostpage"),
    path("jobpost/<int:id>",views.JobDetailSubmit,name="jobpost"),
    path("tableview/",views.TableView,name="tableview"),
    path("jobpostlistpage/",views.JobListPage,name="joblistpage"),
    path("joblist/",views.CandidateJobListPage,name="joblist"),
    path("companylogout/",views.CompanyLogout,name="companylogout"),
    path("candidatelogout/",views.CandidateLogout,name="candidatelogout"),
    path("detailspage/<int:id>",views.DetailsPage, name="detailspage"),
    path("applypage/",views.ApplyPage,name="apply"),
]