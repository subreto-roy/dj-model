from django.urls import path
from .import views
urlpatterns = [
    # path('stu/',views.Studentinfo),
    path('registration/',views.showformdata), 
]
