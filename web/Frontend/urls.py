from django.urls import path

from Frontend import views

urlpatterns = [
    path('web/', views.web, name='web')
]