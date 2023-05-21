from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("",views.initial, name = 'inital'),
    path("home",views.index, name = 'home'),
    path("home-owner",views.index1, name = 'home-owner'),
    path("about",views.about,name = 'about'),
    path("about-owner",views.about1,name = 'about-owner'),
    path("vehicles", views.vehicles, name= "vehicles"),
    path("vehicles1", views.vehicles1, name= "vehicles1"),
    path("vehicles2", views.vehicles2, name= "vehicles2"),
    path("register", views.register, name="register"),
    path("register-owner", views.registerowner, name="register-owner"),
    path("signin", views.signin, name="signin"),
    path("signin-owner", views.signinowner, name="signin-owner"),
    path("signout",views.signout,name = "signout"),
    path("bill",views.order,name = "bill"),
    path("bill1",views.order1,name = "bill1"),
    path("bill2",views.order2,name = "bill2"),
    path("contact",views.contact,name = 'contact'),
    path("contact-owner",views.contact1,name = 'contact-owner'),
    path("adminhome",views.adminhome,name = 'adminhome'),
    path("handle",views.handle,name = 'handle'),
    path("handle-owner",views.handle1,name = 'handle-owner'),
    path("payment", views.payment, name="payment"),
    path("bank-details", views.ownerbankdetails, name="bank-details"),
    path("faqs", views.faqs, name="faqs"),
    path("faqs-owner", views.faqs1, name="faqs-owner"),
    path("profile", views.profile, name="profile"),
    path("settings", views.settings, name="settings"),
    path("settings1", views.settings1, name="settings1"),
    path("help", views.help, name="help"),
    path("help1", views.help1, name="help1"),
    path("help2", views.help2, name="help2"),
    path("personal", views.OwnerInfo, name="personal"),
    path("docs", views.docs, name="docs"),
    path("vehicle-pdfs", views.OwnerVehicleDetails, name="vehicle-pdfs"),
    ]