from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Notes
from .error import EmptyField, MaxCharacters, NonInteger, ExceedDatabase


# Create your views here.
def home(request):
    notes = Notes.objects.order_by('pub_date')
    return render(request, 'notes/index.html', {'notes': notes})


def new_note(request):
    # Get the data from the input and textarea in the form
    title_note = request.POST.get('title-note').strip()
    content_note = request.POST.get('content-note').strip()
    date_note = timezone.now()

    try:
        if not title_note or not content_note:
            raise EmptyField
        elif len(title_note) > 100:
            raise MaxCharacters
    except EmptyField:
        error_message = 'Por favor, el campo no puede estar vacío'
        notes = Notes.objects.order_by('pub_date')
        return render(request, 'notes/index.html', {'error_message': error_message, 'notes': notes})
    except MaxCharacters:
        error_message = 'El título no puede contener más de cien caracteres'
        notes = Notes.objects.order_by('pub_date')
        return render(request, 'notes/index.html', {'error_message': error_message, 'notes': notes})
    else:
        # Use the Notes to create a new object and save it to the database
        Notes.objects.create(title_note=title_note, content_note=content_note, pub_date=date_note)

    return HttpResponseRedirect(reverse('notes:home'))


def delete_note(request, note_id):
    try:
        last_note = Notes.objects.order_by('-pub_date')[0].id
        if note_id > last_note:
            raise ExceedDatabase
    except ExceedDatabase:
        print("This id doesn't exist in the database")
    else:
        note = Notes.objects.get(pk=note_id)
        note.delete()
        return HttpResponseRedirect(reverse('notes:home'))