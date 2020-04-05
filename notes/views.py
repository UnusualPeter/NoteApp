from django.shortcuts import render

from .models import Notes
from .error import EmptyField, MaxCharacters


# Create your views here.
def home(request):
    notes = Notes.objects.order_by('pub_date')
    context = {
        'notes': notes
    }
    return render(request, 'notes/index.html', context)


def new_note(request):
    # Get the data from the input and textarea in the form
    title_note = request.POST.get('title-note').strip()
    content_note = request.POST.get('content-note').strip()

    try:
        if not title_note or not content_note:
            raise EmptyField
        if len(title_note) > 100:
            raise MaxCharacters
    except EmptyField:
        error_message = 'Por favor, el campo no puede estar vacío'
        print(error_message)
    except MaxCharacters:
        error_message = 'El título no puede contener más de cien caracteres'
        print(error_message)
    else:
        # Use the Notes to create a new object and save it to the database
        Notes.objects.create(title_note=title_note, content_note=content_note)

    return render(request, 'notes/index.html')
