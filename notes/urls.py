from django.urls import path
from . import views

# Set the urls for the app
app_name = 'notes'
urlpatterns = [
    path('', views.home, name='home'),
    path('new_note', views.new_note, name='new_note')
]