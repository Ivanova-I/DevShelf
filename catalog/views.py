from urllib import error
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import ProtectedError
from .models import Technology, Tag
from .forms import TechnologyForm, TagForm


def catalog_home(request):
    technologies = Technology.objects.all()
    return render(request,'catalog/home.html',
                  {'technologies': technologies})
def technology_detail(request,pk):
    technology = get_object_or_404(Technology, pk=pk)
    return render(request,'catalog/technology_detail.html',{'technology':technology})

@login_required

def technology_create(request):
    if request.method == 'POST':
        form = TechnologyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog_home')
    else:
        form = TechnologyForm()
    return render(request,'catalog/technology_create.html',{'form':form})

@login_required

def technology_edit(request,pk):
    technology = get_object_or_404(Technology, pk=pk)
    if request.method == 'POST':
        form = TechnologyForm(request.POST,instance=technology)
        if form.is_valid():
            form.save()
            return redirect('catalog_home')
    else:
        form = TechnologyForm(instance=technology)
    return render(request,'catalog/technology_edit.html',{'form':form, 'technology':technology})

@login_required

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

def tag_home(request):
    tag = Tag.objects.all()
    return render(request,'catalog/tag_home.html',{'tag':tag})

@login_required

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_home')
    else:
        form = TagForm()
    return render(request, 'catalog/tag_create.html',{'form':form})

@login_required

def tag_edit(request,pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST,instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tag_home')
    else:
        form = TagForm(instance=tag)
    return render(request, 'catalog/tag_edit.html',{'form':form})

@login_required

def tag_delete(request,pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('tag_home')


    return render(request, 'catalog/tag_delete.html', {'tag': tag})
