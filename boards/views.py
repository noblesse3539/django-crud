# import 순서!!!

# 1. 파이썬 표준 라이브러리 ex) os, random

# 2. Core Django : 장고 프레임워크에 있는 것
from django.shortcuts import render, redirect
# 3. 3rd party library : django_extensions

# 4. 장고 프로젝트 App
from .models import Board # 명시적 상대 import vs 암묵적 상대 import (from models import Board)



# Create your views here.
def index(request):
    return render(request, 'boards/index.html')
    
def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board(title=title, content=content)
    board.save()
    # return render(request, 'boards/create.html', {'board': board})
    return redirect('/boards/')
    