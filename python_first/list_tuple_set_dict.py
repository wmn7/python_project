#!/usr/bin/env python3

#list_study
course = ['Linux','Python','Vim','C++']
print(course)
course.append('PHP')
print(course)
print("course[0]:",course[0])
print(len(course))
course.insert(0,'Java')
print(course)
print(course.count('Java'))
new_course=['A','B']
course.extend(new_course)
print(course)

#tuple_study
tuple_course = ('tuple',course)
print(tuple_course)

tuple_course[1].append('C')
print(tuple_course)

#set_study

set_course={'Linux','c++','Linux'}
dou = 'Linux' in set_course
print(dou)
set_course.add('Python')
set_course.remove('c++')
print(set_course)

set1={1,2,3,4}
set2={3,4,5,6}

print(set1.union(set2))
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)

#dict_study

dict_course = {1:'Linux',2:'Vim'}
print(dict_course)
print(dict_course.get(1,'Error'))
print(dict_course.get(3,'Error'))

dict_course=dict(((1,'Python'),(2,'Java')))
print(dict_course)
dict_course[3]='C++'
print(dict_course)


print(dict_course.items())
print(dict_course.keys())
print(dict_course.values())

for i in dict_course.items():
    print(i)





