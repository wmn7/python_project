#!/usr/bin/env python3
import sys

#print(sys.argv)

def salary_calculate(salary_raw):
    salary = salary_raw*(1-0.165)
    if salary<3500:
        salary_need = 0
    else:
        salary_need = salary-3500

    if salary_need<=1500:
        salary_push = salary_need*0.03
    elif 1500<salary_need<=4500:
        salary_push = salary_need*0.1-105
    elif 4500<salary_need<=9000:
        salary_push = salary_need*0.2-555
    elif 9000<salary_need<=35000:
        salary_push = salary_need*0.25-1005
    elif 35000<salary_need<55000:
        salary_push = salary_need*0.3-2755
    elif 55000<salary_need<80000:
        salary_push = salary_need*0.35-5505
    elif salary_need>80000:
        salary_push = salary_need*0.45-13505
    return (format((salary-salary_push),'.2f'))


if __name__=='__main__':
    try:
        num_salary = sys.argv[1:]
        name_dict={}
        for i in num_salary:
            temp=i.split(':')
            name_dict[temp[0]]=int(temp[1])
        for i in name_dict.keys():
            print(str(i)+':'+str(salary_calculate(name_dict[i])))
    except:
        print('Parameter Error')
        exit()

'''
try:
    salary = int(sys.argv[1])
except:
    print("Parameter Error")
    exit()
'''
