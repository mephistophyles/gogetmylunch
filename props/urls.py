from django.urls import path
from . import views

urlpatterns = [
    path('api/prop/', views.PropListCreate.as_view() ),
]