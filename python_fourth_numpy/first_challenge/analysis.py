#!/usr/bin/env python3
import sys
import json
import pandas as pd
import numpy as np
from pandas import DataFrame

#print(sys.argv)

def analysis(filename, user_id):
    
    times = 0
    minutes = 0


    with open(filename,'r') as file:
        data_list = json.loads(file.read())

    data = [[d['user_id'], d['minutes']] for d in data_list]
        
    df = pd.DataFrame(data, columns=['user_id', 'minutes'])

    
    minutes = df[df['user_id']==user_id]['minutes'].sum()
    times = df[df['user_id']==user_id]['minutes'].count()

    if np.isnan(minutes):
        return 0,0
    else:
        return times, minutes

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        user_id = int(sys.argv[2])
    except:
        print('Error')
        exit()

    times,minutes = analysis(filename,user_id)
    print(times,minutes)

