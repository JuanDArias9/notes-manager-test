from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Note
from .forms import NoteForm

def notes_view(request):
    form = NoteForm()
    notes = Note.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡La nota ha sido creada exitosamente!")
            return redirect('notes')

    return render(request, 'notes/notes.html', {'form': form, 'notes': notes})