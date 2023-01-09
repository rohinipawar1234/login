from django.urls import path
from app.views import*

urlpatterns = [
    path('index',Index,name="index"),
    path('',Loginpage,name="loginpage"),
    path('',Updatepage,name="updatedata"),
    path('showdata/',Showdata,name="showdata"),
    path("registerdata",Register,name="registerdata"),
    path('showdata/',Showdata,name="showdata"),
    path('deletedata/<int:id>',Deletedata,name="deletedata"),
    
]


