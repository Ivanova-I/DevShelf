from django.core.exceptions import PermissionDenied
from django.db.models import ProtectedError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Resource, Note
from .forms import ResourceForm, NoteForm, NoteEditForm
from catalog.models import Technology


def resources_home(request):
    resources = Resource.objects.all()
    technologies = Technology.objects.all()
    technology_id = request.GET.get('technology')
    if technology_id:
        resources = resources.filter(technology_id=technology_id)
    sort = request.GET.get('sort')
    if sort == 'title':
        resources = resources.order_by('title')
    elif sort == 'rating':
        resources = resources.order_by('-rating')
    elif sort == 'duration':
        resources = resources.order_by('estimated_minutes')
    return render(request,'resources/home.html',
                  {'resources': resources,'technologies': technologies})

def resources_detail(request,pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request,'resources/resources_detail.html',{'resource':resource})

@login_required
@user_passes_test(lambda u: u.is_staff)
def resources_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources_home')
    else:
        form = ResourceForm()

    return render(request,  'resources/resources_create.html',{'form':form})


@login_required
@user_passes_test(lambda u: u.is_staff)
def resources_edit(request,pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resources_home')
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'resources/resources_edit.html',{'form':form})


@login_required
@user_passes_test(lambda u: u.is_staff)
def resources_delete(request,pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        try:
            resource.delete()
            return redirect('resources_home')
        except ProtectedError:
            return render(request, 'resources/resources_delete.html', {'resource': resource,
                                                                      'error': 'This resource cannot be deleted because it is used by one or more objects.'})
    return render(request,'resources/resources_delete.html',{'resource':resource})

def note_home(request):
    note = Note.objects.all()
    return render(request,'resources/note_home.html',{'note':note})

def note_detail(request,pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request,'resources/note_detail.html',{'note':note})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()

            return redirect('note_home')
    else:
        form = NoteForm()
    return render(request, 'resources/note_create.html',{'form':form})

@login_required
def note_edit(request,pk):
    note = get_object_or_404(Note, pk=pk)
    if note.user != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_home')
    else:
        form = NoteEditForm(instance=note)
    return render(request, 'resources/note_edit.html',{'form':form})

@login_required
def note_delete(request,pk):
    note = get_object_or_404(Note, pk=pk)
    if note.user != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        try:
            note.delete()
            return redirect('note_home')
        except ProtectedError:
            return render(request, 'resources/note_delete.html', {'note': note,
                                                                  'error':'This note cannot be deleted because it is used by one or more objects.'})
    return render(request, 'resources/note_delete.html',{'note':note})