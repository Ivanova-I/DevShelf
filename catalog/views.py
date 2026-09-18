from django.shortcuts import get_object_or_404, render, redirect
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

