from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from .models import Resource
from .forms import ResourceForm

def resources_home(request):
    resources = Resource.objects.all()
    return render(request,'resources/home.html',
                  {'resources': resources})

def resources_detail(request,pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request,'resources/resources_detail.html',{'resource':resource})

def resources_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources_home')
    else:
        form = ResourceForm()

    return render(request,  'resources/resources_create.html',{'form':form})

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


# Create your views here.
