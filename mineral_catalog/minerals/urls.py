from django.urls import path

from . import views

urlpatterns = [
    path('', views.mineral_list, name="list"),
    path('minerals/<pk>', views.mineral_detail, name='detail')
]







