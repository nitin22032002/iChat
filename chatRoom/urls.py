from django.urls import path
from . import views
urlpatterns=[
    path("",views.landingPage,name="Home Page"),
    path("signin/",views.signIn,name="SignIn Page"),
    path("authentication/auth/o/1/log/Signup",views.addUser,name="SignUp"),
    path("authentication/auth/o/1/log/Login",views.login,name="SignIn"),
    path("signin/",views.signIn,name="SignIn Page"),
    path("joinmeeting/",views.joinMeeting,name="Join Meeting Page"),
    path("waitingroom/",views.waitingRoom,name="Waiting Room Page"),
    path("verifyuser/",views.otp,name="otp page"),
    path("adduser/",views.verifyUser,name="Verify User"),
    path("resend/",views.sendOtps,name="Send Otp"),
    path("logout/",views.logout,name="Logout"),
    path("deletemeeting/",views.deleteMeeting,name="delete Meeting"),
    path("roomdetails/",views.getRoomDeatils,name="Room Deatils"),
    path("meetinglist/",views.allMetings,name="All Meetings"),
    path("createmeeting/",views.createMeeting,name="createMeeting page"),
    path("create/createmeeting",views.saveMeeting,name="createMeeting"),
    path("join/stand",views.joinPerson,name="join"),
    path("validate",views.validate,name="validate"),
    path("cancel/",views.cancel,name="Cancel Meeting"),
    path("meetingarea/",views.meetingArea,name="Meeting Area"),
]