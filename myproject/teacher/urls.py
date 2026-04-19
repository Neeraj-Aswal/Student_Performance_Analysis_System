from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('choose-semester/', views.choose_semester, name='choose_semester'),
    path('one-semester/', views.one_semester, name='one_semester'),
    path('multi-semester/', views.multi_semester, name='multi_semester'),
]