#!/usr/bin/env python3
import sys
import json
import pandas as pd
import numpy as np
from pandas import DataFrame

import matplotlib.pyplot as plt

#print(sys.argv)

def analysis(filename):
    
    times = 0
    minutes = 0


    with open(filename,'r') as file:
        data_list = json.loads(file.read())

    data = [[d['user_id'], d['minutes']] for d in data_list]
        
    df = pd.DataFrame(data, columns=['user_id', 'minutes'])

    #获取所有的user_id
    user_id = {d['user_id'] for d in data_list}
    #去重并排序
    user_id = list(user_id)
    user_id.sort()
    #print(user_id[:5])

    
    minutes = [df[df['user_id']==userid]['minutes'].sum() for userid in user_id]

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')

    ax.plot(user_id,minutes)
    plt.show()
    

if __name__ == '__main__':
    analysis('user_study.json')

