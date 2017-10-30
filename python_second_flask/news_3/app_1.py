#!/usr/bin/env python3
# -*-coding:utf-8 -*-

import os
import json
from collections import OrderedDict
from datetime import datetime

'''
设置Flask程序的入口－－app.py是flask程序的入口
export FLASK_APP=app.py
flask运行命令，port修改运行的端口号
FLASK_DEBUG=1 FLASK_APP=app.py flask run --port=3000
'''

from flask import Flask, make_response, render_template, request
from flask_sqlalchemy import SQLAlchemy

'''
创建一个app对象
'''
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# 连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@Wangmaonan1@localhost/news'
db = SQLAlchemy(app)

class File(db.Model):
    #文章的ID
    id = db.Column(db.Integer,primary_key=True)
    #文章名称
    title = db.Column(db.String(80),unique=True)
    #文章创建时间
    created_time = db.Column(db.DateTime)
    #文章的内容
    content = db.Column(db.Text)

    #文章的分类
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('posts',lazy='dynamic'))

    def __init__(self,title,category,content,created_time=None):
        self.title = title
        if created_time is None:
            created_time = datetime.utcnow()
        self.category = category
        self.content = content

    def __repr__(self):
        return '<File %r>' % self.title

class Category(db.Model):
    #类别的ID
    id = db.Column(db.Integer,primary_key=True)
    #类别的名称
    name = db.Column(db.String(80))

    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return '<Category %r>' % self.name

db.create_all()


#插入数据
def insert_datas():
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', java, 'File Content - Java is cool!',datetime.utcnow())
    file2 = File('Hello Python', python, 'File Content - Python is cool!',datetime.utcnow())
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()


category = Category.query.all()

print(category)

category_name = Category.query.filter_by(name='python').first()

#通过.name访问name字段的
print(category_name.name)


'''

# 定义一个过滤器,就是一个函数
def hidden_email(email):
    parts = email.split('@')
    parts[0] = '*******'
    return '@'.join(parts)

app.add_template_filter(hidden_email)

'''



#自定义错误处理页面
@app.errorhandler(404)
def not_found(error):
    #返回404页面和404状态码
    return render_template('404.html'),404


#路由可以理解为访问网站访问的链接
@app.route('/')
def index():
    File.query.all
'''
@app.route('/')
def index():

    title_name = []
    file_name = os.listdir('./files')

    for name in file_name:
        with open('./files/'+name,'r') as file:
            result = json.loads(file.read())
            title_name.append(result['title'])

    return render_template('index.html',title_name = title_name)
'''

# 参数用尖括号括起来
@app.route('/files/<filename>')
def user_index(filename):
    #render_template函数第一个参数是模板,为一个html文件,里面有jinja的语法
    try:
        file_name = OrderedDict()
        
        with open('./files/'+filename+'.json','r') as file:
            result = json.loads(file.read())
            for i in result:
                file_name[i] = result[i]

        resp = render_template('file_index.html',file_name = file_name)
        
        return resp
    except:
        return render_template('404.html'),404    



if __name__ == '__main__':
    app.run()
