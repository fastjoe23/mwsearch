from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Midwife, MWRequest
from .forms import NewMWRequestForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = NewMWRequestForm(request.post)
        if form.is_valid():
            mwrequest = form.save(commit=False)
            mwrequest.save()
            return redirect('list_mws')
    else:
        form = NewMWRequestForm()
    return render(request, 'home.html', {'form': form})


class MWListView(ListView):
    model = Midwife
    context_object_name = 'midwifes'
    template_name = 'list_mws.html'
