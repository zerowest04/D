from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Diary

# Create your views here.
def home(request):
    diary = Diary.objects.all()
    total_num = Diary.objects.count()
    return render(request, "home.html", {'total_num' : total_num})

def index(request):
    diary = Diary.objects.all()
    return render(request, "index.html", {'diary' : diary})
    
def detail(request, id):
    diary  = get_object_or_404(Diary, pk = id)
    return render(request, 'detail.html', {'diary': diary})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_diary = Diary()
    new_diary.title = request.POST['title']
    new_diary.body =  request.POST['body']
    new_diary.pub_date = timezone.now()
    new_diary.save()
    return redirect('detail', new_diary.id) # no render

def edit(request, id):
    edit_diary = Diary.objects.get(id = id)
    return render(request, 'edit.html', {'diary': edit_diary})

def update(request, id):
    update_diary = Diary.objects.get(id = id)
    update_diary.title = request.POST['title']
    update_diary.body =  request.POST['body']
    update_diary.pub_date = timezone.now()
    update_diary.save()
    return redirect('detail', update_diary.id) # no render
 
def delete(request, id):
    deleter_diary = Diary.objects.get(id = id)
    deleter_diary.delete()
    return redirect('home') # no render