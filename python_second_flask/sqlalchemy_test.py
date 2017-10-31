from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

engine = create_engine('mysql://root:Wangmaonan1@localhost/shiyanlou')

user_data = engine.execute('select * from user').fetchall()

print(user_data)

'''
首先导入了 create_engine, 该方法用于创建 Engine 实例，传递给 create_engine 的参数定义了 MySQL 服务器的访问地址，其格式为 mysql://<user>:<password>/<host>/<db_name>

接着通过 engine.execute 方法执行了一条 SQL 语句，查询了 user 表中的所有用户

'''


'''
如果想使 Python 类映射到数据库表中，需要基于 SQLAlchemy 的 declarative base class，也就是宣言基类创建类。当基于此基类，创建 Python 类时，就会自动映射到相应的数据库表上。创建宣言基类，可以通过 declarative_base 方法进行
'''

Base = declarative_base()

'''
创建基类以后，创建 User 类
'''

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<User(name=%s)>" % self.name

'''
如果想通过 User 查询数据库该怎么办呢？需要先引入 Session。Session 是映射类和数据库沟通的桥梁，包含事务管理功能。
'''

Session = sessionmaker(bind=engine)
session = Session()

print(session.query(User).all())

# 创建数据库表

class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer,ForeignKey('user.id'))
    teacher = relationship('User')

    def __repr__(self):
        return '<Course(name=%s)>' % self.name


'''
SQLAlchemy 中可以使用 ForeignKey 设置外键。设置外键后，如果能够直接从 Course 的实例上访问到相应的 user 表中的记录会非常方便，而这可以通过 relationship 实现。上面的代码通过 relationship 定义了 teacher 属性，这样就可以直接通过 course.teacher 获取相应的用户记录
'''

class Lab(Base):
    __tablename__ = 'lab'

    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    course_id = Column(Integer,ForeignKey('course.id'))
    course = relationship('Course',backref = 'labs')

    def __repr__(self):
        return '<Lab(name=%s)>' % self.name

# 创建lab表
Base.metadata.create_all(engine)

course = session.query(Course).first()

lab1 = Lab(name='ORM 基础', course_id=course.id)

lab2 = Lab(name='关系数据库', course=course)

# 首先将数据add到session中
session.add(lab1)

session.add(lab2)

session.commit()

# 删除对象
session.delete(lab1)
session.commit()