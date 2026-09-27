from django.db.models import ProtectedError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import LearningPath
from .forms import LearningPathForm

def learning_home(request):
    learn = LearningPath.objects.all()
    return render(request,'learning/home.html',
                  {'learn': learn})

def learning_detail(request,pk):
    learn = get_object_or_404(LearningPath, pk=pk)
    return render(request,'learning/learning_detail.html',{'learn':learn})

@login_required
@user_passes_test(lambda u: u.is_staff)
def learning_create(request):
    if request.method == 'POST':
        form = LearningPathForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_home')
    else:
        form = LearningPathForm()

    return render(request,  'learning/learning_create.html',{'form':form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def learning_edit(request,pk):
    learn = get_object_or_404(LearningPath, pk=pk)
    if request.method == 'POST':
        form = LearningPathForm(request.POST, instance=learn)
        if form.is_valid():
            form.save()
            return redirect('learning_home')
    else:
        form = LearningPathForm(instance=learn)
    return render(request, 'learning/learning_edit.html',{'form':form, 'learn':learn})


@login_required
@user_passes_test(lambda u: u.is_staff)
def learning_delete(request,pk):
    learn = get_object_or_404(LearningPath, pk=pk)
    if request.method == 'POST':
        try:
            learn.delete()
            return redirect('learning_home')
        except ProtectedError:
            return render(request, 'learning/learning_delete.html', {'learn': learn,
                                                                      'error': 'This LearningPath cannot be deleted because it is used by one or more objects.'})
    return render(request,'learning/learning_delete.html', {'learn': learn,})
