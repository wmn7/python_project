#!/usr/bin/env python3
import sys

#print(sys.argv)

try:
    salary = int(sys.argv[1])
except:
    print("Parameter Error")
    exit()

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

print(format(salary_push,".2f"))
