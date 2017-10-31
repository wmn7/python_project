from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# 连接数据库
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Wangmaonan1@localhost/news'
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
        if self.created_time is None:
            self.created_time = datetime.utcnow()
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
    file2 = File('Hello Python' , python, 'File Content - Python is cool!',datetime.utcnow())
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()

#insert_datas()

file = File.query.all()

for i in file:
    print(i.title," : ",i.id," : ",i.content," : ",i.category.name," : ",i.created_time,end="\n")

print('-----------------')


category_name = Category.query.filter_by(name='python').first()

#通过.name访问name字段的
print(category_name.name)