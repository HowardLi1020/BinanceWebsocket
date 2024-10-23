# my_app/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')  # 渲染 index.html 模板
