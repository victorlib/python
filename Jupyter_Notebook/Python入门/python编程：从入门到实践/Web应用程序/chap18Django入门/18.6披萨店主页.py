"""
创建主页（三个阶段： 定义URL、 编写视图和编写模板）
1. 在pizzeria/pizzeria/urls.py中：
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    --snip--
    path('', include('pizzas.urls'))
]

在pizzeria/pizzas文件夹中创建urls.py，文件内容：
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]


2. 在pizzeria/pizzas/views.py中：
def index(request):
    return render(request, 'pizzas/index.html')


3. 在pizzeria/pizzas文件夹中创建templates/pizzas/index.html
"""