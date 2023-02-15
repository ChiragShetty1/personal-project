from django.urls import path
from helloapp import views
urlpatterns = [
    path('',views.chirag),
    path("index",views.index),
    path("contact",views.contact),
    path('chirag',views.chirag),
    
]
