"""
1. 创建一个新文件夹pizzeria
cd pizzeria

2. 进入该文件夹，创建虚拟环境：
python -m venv env

3. 激活环境
env\Scripts\activate

4. 安装Django
pip install Django

5. 新建项目
django-admin.py startproject pizzeria .

6. 创建数据库
python manage.py migrate

7. 启动服务器
python manage.py runserver

8. 创建应用程序
python manage.py startapp pizzas

9. 定义模型
class Pizza(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


10. 激活模型
在settings.py中，在INSTALLED_APPS元组中添加自己刚刚创建的应用程序
INSTALLED_APPS = (
    --snip--
    'django.contrib.staticfiles',

    # 我的应用程序
    'pizzas',
)
python manage.py makemigrations learning_logs
python manage.py migrate

11. 创建超级用户
python manage.py createsuperuser

12. 向管理网站注册模型，在admin.py中
from django.contrib import admin
from learning_logs.models import Topic
admin.site.register(Topic)

13. 使用shell来查看你输入的数据
python manage.py shell


"""