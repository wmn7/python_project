#!/usr/bin/env python3
# -*-coding:utf-8 -*-

import os
import json
from collections import OrderedDict


'''
设置Flask程序的入口－－app.py是flask程序的入口
export FLASK_APP=app.py
flask运行命令，port修改运行的端口号
FLASK_DEBUG=1 FLASK_APP=app.py flask run --port=3000
'''

from flask import Flask, make_response, render_template, request

'''
创建一个app对象
'''
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# 定义一个过滤器
def hidden_email(email):
    parts = email.split('@')
    parts[0] = '*******'
    return '@'.join(parts)

app.add_template_filter(hidden_email)

#自定义错误处理页面
@app.errorhandler(404)
def not_found(error):
    #返回404页面和404状态码
    return render_template('404.html'),404


#路由可以理解为访问网站访问的链接
@app.route('/')
def index():

    title_name = []
    file_name = os.listdir('./files')

    for name in file_name:
        with open('./files/'+name,'r') as file:
            result = json.loads(file.read())
            title_name.append(result['title'])

    return render_template('index.html',title_name = title_name)


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
