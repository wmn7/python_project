#!/usr/bin/env python3

class Dog(object):
    def __init__(self,name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name=value
    def bark(self):
        #bark方法
        print(self.get_name()+' is making sound wang wang wang')

class Cat(object):
    def __init__(self,name):
        self._name = name
    def get_name(self):
        return self._name.lower().capitalize()
    def set_name(self,value):
        self._name=value
    def bark(self):
        #bark方法
        print(self.get_name()+' is making sound miao miao miao')

dog = Dog('旺财')
dog.bark()      

cat = Cat('kitty')
cat.bark()

print('----------------------')

# 继承－－－对上面两个动物再做一个抽象类
class Animal(object):
    def __init__(self,name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name = value
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(self.get_name()+' is making sound wang wang wang')

class Cat(Animal):
    def make_sound(self):
        print(self.get_name()+' is making sound miao miao miao')

dog = Dog('旺财')
cat = Cat('Kitty')
dog.make_sound()
cat.make_sound()

print('---------------------')

# 多态－－使用同一方法对不同的对象产生不同的结果
animals = [Dog('旺财'),Cat('Kitty'),Dog('来福'),Cat('Betty')]

for aniamal in animals:
    aniamal.make_sound()

print('-----------------------')

# 私有属性和方法

'''
在 Java 和 C++ 中，可以用 private 和 protected关键字修饰属性和方法，它们控制属性和方法能否被外部或者子类访问.abs
在 Python 中约定在属性方法名前添加 __ （两个下划线 _）来拒绝外部的访问。
'''

class shiyanlou:
    __pricate_name='shiyanlou'
    def __get_private_name(self):
        return self.__pricate_name


'''
为什么说是“约定”，因为 Python 中不是绝对的私有，还是通过 obj._Classname__privateAttributeOrMethod 来访问
'''

print(shiyanlou()._shiyanlou__pricate_name)

# 静态变量和类方法

'''
静态变量和类方法是可以直接从类访问，不需要实例化对象就能访问。假设上面例子中的动物它们都是 Jack 养的，那么就可以在 Animal 类中用一个静态变量表示，一般声明在 __init__ 前面
'''

class Animal(object):
    owner='jack'
    def __init__(self,name):
        self._name=name

print(Animal.owner)

class Cat(Animal):
    def __init__(self,name):
        self._name = name
    def make_sound(self):
        print('bark')

print(Cat.owner)

Cat('cat').make_sound()


print('------------------')

#property--将方法变成属性
class Cat(Animal):
    def __init__(self,name):
        self._name = name
    @property
    def make_sound(self):
        print('bark_property')



Cat('Kitty').make_sound

#静态方法

class Cat(Animal):
    def __init__(self,name):
        self._name = name
    @property
    def make_sound(self):
        print('bark')
    @staticmethod
    def order_aninal_food():
        print('staticmethod_123')

Cat.order_aninal_food()


