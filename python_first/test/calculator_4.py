#!/usr/bin/env python3

# ./calculator.py -c test.cfg -d user.csv -o gongzi.csv

from multiprocessing import Process, Queue
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

# 读取配置文件信息--保存成字典类型config_dict
def read_config(queue1,configfile):
    config_dict = {}
    try:
        with open(configfile,'r') as configfile:
            for x in configfile:
                cash = x.split('=')
                config_dict[cash[0].strip()]=float(cash[1].strip())
        tax = config_dict['YangLao'] + config_dict['YiLiao'] + config_dict['ShiYe'] + config_dict['GongShang'] + config_dict['ShengYu'] + config_dict['GongJiJin']
        queue1.put([config_dict,tax])
    except:
        print('filename error')
        sys.exit(-1)

#print(config_dict)


# 读取员工信息--保存成list类型employ_dict
# 读取csv文件
def read_employ(queue1,queue2,employ_data_file):
    data = queue1.get()
    config_dict = data[0]
    tax = data[1]
    employ_dict = []
    try:
        with open(employ_data_file,'r') as user_file:
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

    result = ['{},{},{:.2f},{:.2f},{:.2f}'.format(i[0],i[1],i[2],i[3],i[4]) for i in employ_dict]

    for i in range(len(result)):
        result[i] = result[i].split(',')
    
    queue2.put(result)

#result = [['{:.2f}'.format(i) for i in j] for j in employ_dict]

#print(result)


# 写入csv文件
def writer_csv(queue2,employ_o_data_file):
    result = queue2.get()
    try:
        with open(employ_o_data_file,'w') as user_file:
            writer = csv.writer(user_file)
            for i in range(len(result)):
                writer.writerow(result[i])
    except:
        print('filename error')
        sys.exit(-1)

def main(queue1,queue2,configfile,employ_data_file,employ_o_data_file):
    p1 = Process(target=read_config,args=(queue1,configfile))
    p2 = Process(target=read_employ,args=(queue1,queue2,employ_data_file))
    p3 = Process(target=writer_csv,args=(queue2,employ_o_data_file))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()


if __name__ == '__main__':
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
    queue1 = Queue()
    queue2 = Queue()
    main(queue1,queue2,configfile,employ_data_file,employ_o_data_file)
