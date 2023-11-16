from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    return render(request,'base.html')

def go_login(request):
    return render(request,'login.html')

def add_drug(request):
    context = {"drug_type" : d_type.objects.all()}
    if request.method =="POST":
        table = drug()
        table.drug_name = request.POST['drug_name']
        table.drug_type = d_type.objects.get(type_id = request.POST['drug_type'])
        table.drug_qty = request.POST['drug_qty']
        table.drug_exp = request.POST['drug_expired']
        table.save()
        return redirect('/manage_drug')
    return render(request,'add_drug.html',context)

def manage_drug(request):
    show_drug = drug.objects.all()
    context = {'drug' : show_drug}
    return render(request,'manage_drug.html',context)

def delete_drug(request,pk):
    table = drug.objects.get(drug_id=pk)
    table.delete()
    return redirect('/manage_drug')