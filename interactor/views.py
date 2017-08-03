from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Friends
from .forms import InputForm

def index(request):
    return render(request, 'interactor/index.html')

def input_page(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            new_item = Friends(name = form.cleaned_data['name'], website = form.cleaned_data['website'], LOR_contact = form.cleaned_data['LOR_contact'], ext_contact = form.cleaned_data['ext_contact'], notes = form.cleaned_data['notes'], plans = form.cleaned_data['plans'])
            new_item.save()
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = InputForm()

    return render(request, 'interactor/input.html', {'form': form})

def friends_list(request):
    total_list = Friends.objects.all()
    context = {'total_list': total_list}
    return render(request, 'interactor/list.html', context)

def friend_detail(request, friend_id):
    return HttpResponse("Here is your friend")

def thanks(request):
    return HttpResponse("Thanks!")


