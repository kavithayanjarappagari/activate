from django.urls import path
from app1 import views
urlpatterns=[
    path('',views.home,name="homepage"),
    path('login/',views.login_view,name="loginpage"),
    path('create',views.create,name="createpage"),
    path('display',views.display,name="displaypage"),
    path('profile',views.profile,name="profilepage"),
    path('register',views.register,name="registerpage"),
    path('logout',views.logoutV,name="logoutpage"),
]