from urllib import error

from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import ProtectedError
from .models import Technology
from .forms import TechnologyForm
def catalog_home(request):
    technologies = Technology.objects.all()
    return render(request,'catalog/home.html',
                  {'technologies': technologies})
def technology_detail(request,pk):
    technology = get_object_or_404(Technology, pk=pk)
    return render(request,'catalog/technology_detail.html',{'technology':technology})

def technology_create(request):
    if request.method == 'POST':
        form = TechnologyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog_home')
    else:
        form = TechnologyForm()
    return render(request,'catalog/technology_create.html',{'form':form})

def technology_edit(request,pk):
    technology = get_object_or_404(Technology, pk=pk)
    if request.method == 'POST':
        form = TechnologyForm(request.POST,instance=technology)
        if form.is_valid():
            form.save()
            return redirect('catalog_home')
    else:
        form = TechnologyForm(instance=technology)
    return render(request,'catalog/technology_edit.html',{'form':form})

def technology_delete(request,pk):
    technology = get_object_or_404(Technology, pk=pk)
    if request.method == 'POST':
        try:
            technology.delete()
            return redirect('catalog_home')
        except ProtectedError:
            return render(request, 'catalog/technology_delete.html',{'technology':technology,
                          'error':'This technology cannot be deleted because it is used by one or more resources.'})

    return render(request,'catalog/technology_delete.html',{'technology':technology})

