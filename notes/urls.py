from django.urls import path
from . import views

# Set the urls for the app
app_name = 'notes'
urlpatterns = [
    path('', views.home, name='home'),
    path('new_note', views.new_note, name='new_note'),
    path('delete_note/<int:note_id>', views.delete_note, name='delete_note'),
    path('edit_note/<int:note_id>', views.edit_note, name='edit_note'),
    path('save_edit_note/<int:note_id>', views.save_edit_note, name='save_edit_note')
]