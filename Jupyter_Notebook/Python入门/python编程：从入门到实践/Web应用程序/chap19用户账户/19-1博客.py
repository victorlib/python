"""
1. 创建一个新文件夹blog
cd blog

2. 进入该文件夹，创建虚拟环境：
python -m venv env

3. 激活环境
env\Scripts\activate

4. 安装Django
pip install Django

5. 新建项目
django-admin.py startproject blog .

6. 创建数据库
python manage.py migrate

7. 启动服务器
python manage.py runserver

8. 创建blogs应用程序
python manage.py startapp blogs

9. 定义模型
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

10. 激活模型
在settings.py中，在INSTALLED_APPS元组中添加自己刚刚创建的应用程序
INSTALLED_APPS = (
    --snip--
    'django.contrib.staticfiles',

    # 我的应用程序
    'blogs',
)

python manage.py makemigrations learning_logs
python manage.py migrate

11. 创建超级用户
python manage.py createsuperuser

12. 向管理网站注册模型，在admin.py中
from django.contrib import admin
from blogs.models import BlogPost
admin.site.register(Topic)



"""