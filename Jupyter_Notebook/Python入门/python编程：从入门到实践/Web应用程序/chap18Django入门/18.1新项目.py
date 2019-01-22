"""
1. 创建一个新文件夹instabook
cd instabook

2. 进入该文件夹，创建虚拟环境：
python -m venv env

3. 激活环境(关闭deactivate)
env\Scripts\activate

4. 安装Django
pip install Django

5. 新建项目(命令末尾的句点让新项目使用合适的目录结构，这样开发完成后可轻松地将应用程序部署到服务器)
django-admin.py startproject instabook .

新创建的instabook项目包含4个文件， __init__.py、settings.py、 urls.py和wsgi.py。
文件settings.py指定Django如何与你的系统交互以及如何管理项目。在开发项目的过程中，我们将修改其中一些设置，并添加一些设置。
文件urls.py告诉Django应创建哪些网页来响应浏览器请求。
文件wsgi.py帮助Django提供它创建的文件，这个文件名是web server gateway interface(Web服务器网关接口)的首字母缩写。

6. 创建数据库
python manage.py migrate

7. 启动服务器
python manage.py runserver
"""