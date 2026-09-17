from django.shortcuts import get_object_or_404, render
from .models import Technology
def catalog_home(request):
    technologies = Technology.objects.all()
    return render(request,'catalog/home.html',
                  {'technologies': technologies})
def technology_detail(request,pk):
    technology = get_object_or_404(Technology, pk=pk)
    return render(request,'catalog/technology_detail.html',{'technology':technology})

# Create your views here.
