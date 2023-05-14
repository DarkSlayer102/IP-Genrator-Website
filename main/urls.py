from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('',views.home,name="home"),
    path('ipv4_result', views.ipv4_result,name="add1"),
    path('ipv4', views.ipv4, name="ipv4"),
    path('ipv6', views.ipv6,name="ipv6"),
    path('ipv6_result', views.ipv6_result,name="add2"),
    path('remove', views.remove,name="remove"),
]