from django.urls import path

from .views import index,Display,Delete_student,Edit_student
urlpatterns=[
    path('',index,name='index'),
    path('display/',Display,name='display'),
    path('delete/<int:id>/',Delete_student,name='delete'),
    path('edit/<int:id>',Edit_student,name='edit')
]