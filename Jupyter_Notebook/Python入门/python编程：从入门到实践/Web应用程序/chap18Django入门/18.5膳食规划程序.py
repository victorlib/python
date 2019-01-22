"""
创建一个新文件夹meal_planner
cd meal_planner
进入该文件夹，创建虚拟环境：
python -m venv env
激活环境
env\Scripts\activate
安装Django
pip install Django
新建项目
django-admin.py startproject meal_planner .
创建数据库
python manage.py migrate
启动服务器
python manage.py runserver
创建应用程序
python manage.py startapp meal_plans

创建主页（三个阶段： 定义URL、 编写视图和编写模板）
1. 在meal_planner/meal_planner/urls.py中：
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    --snip--
    path('', include('meal_plans.urls'))
]

在meal_planner/meal_plans文件夹中创建urls.py，文件内容：
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]


2. 在meal_planner/meal_plans/views.py中：
def index(request):
    return render(request, 'meal_plans/index.html')


3. 在meal_planner/meal_plans文件夹中创建templates/meal_plans/index.html
"""