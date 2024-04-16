from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import MoviechartForm
from .models import Moviechart

@login_required(login_url='login_url')
def add_moviechart(request):
    template_name = 'crud_app/add.html'
    form = MoviechartForm()
    if request.method == "POST":
        form = MoviechartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)
@login_required(login_url='login_url')
def show_moviechart(request):
    template_name = 'crud_app/show.html'
    moviecharts = Moviechart.objects.all()
    context = {'moviecharts': moviecharts}
    return render(request, template_name, context)


def update_moviechart(request,pk):
    template_name = 'crud_app/add.html'
    obj=Moviechart.objects.get(id=pk)
    form = MoviechartForm(instance=obj)
    if request.method == "POST":
        form = MoviechartForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def delete_moviechart(request,pk):
    template_name = 'crud_app/confirm.html'
    obj = Moviechart.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
    return render(request, template_name)

