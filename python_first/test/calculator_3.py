#!/usr/bin/env python3

# ./calculator.py -c test.cfg -d user.csv -o gongzi.csv

import sys
import csv

# 计算个税的函数--返回要交的个税
def employ_tax_calculate(salary):
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
    return (salary_push)

# 读取配置文件路径
try:
    args = sys.argv[1:]
    index = args.index('-c')
    configfile = args[index+1]
    index = args.index('-d')
    employ_data_file = args[index+1]
    index = args.index('-o')
    employ_o_data_file = args[index+1]
except:
    print('filename error')
    sys.exit(-1)

#print(configfile,employ_data_file,employ_o_data_file)


# 读取配置文件信息--保存成字典类型config_dict
config_dict = {}
try:
    with open('./'+str(configfile),'r') as configfile:
        for x in configfile:
            cash = x.split('=')
            config_dict[cash[0].strip()]=float(cash[1].strip())
    tax = config_dict['YangLao'] + config_dict['YiLiao'] + config_dict['ShiYe'] + config_dict['GongShang'] + config_dict['ShengYu'] + config_dict['GongJiJin']
except:
    print('filename error')
    sys.exit(-1)

#print(config_dict)


# 读取员工信息--保存成字典类型employ_dict
# 读取csv文件
employ_dict = []
try:
    with open('./'+str(employ_data_file),'r') as user_file:
        reader = csv.reader(user_file)
        # taxshe为要交的社保
        for i in reader:
            if int(i[1])<config_dict['JiShuL']:
                taxshe = config_dict['JiShuL']*tax
            elif int(i[1])>config_dict['JiShuH']:
                taxshe = config_dict['JiShuH']*tax
            else:
                taxshe = int(i[1])*tax
            employ_wage = int(i[1]) - taxshe - employ_tax_calculate(int(i[1])-taxshe)
            employ_dict.append([int(i[0]),int(i[1]),taxshe,employ_tax_calculate(int(i[1])-taxshe),employ_wage])
            employ_dict.sort()
except:
    print('filename error')
    sys.exit(-1)

result = ['{},{:.2f},{:.2f},{:.2f},{:.2f}'.format(i[0],i[1],i[2],i[3],i[4]) for i in employ_dict]

for i in range(len(result)):
    result[i] = result[i].split(',')

#result = [['{:.2f}'.format(i) for i in j] for j in employ_dict]

#print(result)


# 写入csv文件
try:
    with open('./'+str(employ_o_data_file),'w') as user_file:
        writer = csv.writer(user_file)
        for i in range(len(result)):
            writer.writerow(result[i])
except:
    print('filename error')
    sys.exit(-1)
