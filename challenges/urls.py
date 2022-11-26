from django.urls import path
from . import views
urlpatterns = [ 
    path("",views.index),
    path('<str:month>',views.all, name="month-challenge"),
    path('<int:month>',views.monthly_challenges_by_number )
    ]
