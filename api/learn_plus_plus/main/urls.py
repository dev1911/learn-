from django.urls import path
import views

urlpatterns = [
    path('session/' , views.session , name="session" ),
]