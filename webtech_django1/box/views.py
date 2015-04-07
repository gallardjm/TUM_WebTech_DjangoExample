from django.http import HttpResponse
from box.models import Box
from django.shortcuts import get_object_or_404, render, redirect
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required

#ModelForm to create a box
class BoxCreateForm(ModelForm):
    class Meta:
        model = Box
        fields = ['tag', 'storage']

#ModelForm to update a box, only the storage can change
class BoxUpdateForm(ModelForm):
    class Meta:
        model = Box
        fields = ['storage']

#List all the boxes
def index(request):
    box_list = Box.objects.all() #fetch all the boxes
    return render(request, 'index.html', {'box_list': box_list})

#Create a box   
@login_required 
def create(request):
    form = BoxCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('box:index')
    return render(request, 'create.html', {'form':form})

#Give details about one box
@login_required
def read(request, box_id):
    b = get_object_or_404(Box, id=box_id) #fetch one box, 404 if box_id invalid
    return render(request, 'read.html', {'box': b})

#Update a box 
@login_required
def update(request, box_id):
    box= get_object_or_404(Box, id=box_id)
    form = BoxUpdateForm(request.POST or None, instance=box, initial={'storage': box.storage})
    if form.is_valid():
        form.save()
        return redirect('box:read', box_id)
    return render(request, 'update.html', {'form':form})
    
#Delete a box
@login_required
def delete(request):
    b = get_object_or_404(Box, id=request.POST['box_id']).delete()
    return redirect('box:index')
