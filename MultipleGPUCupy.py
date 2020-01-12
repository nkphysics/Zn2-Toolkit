import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
import cupy as cp
from GpuAccWcupy import ZnCalculation

# This is where we read in the curves

start = float(input('Set Start Test Frequency: '))
end = float(input('Set End Test Frequency: '))
step = float(input('Step: '))

# Stores generated frequencies
nu = np.arange(start,end,step)
# Generates the values of nu based on a set start, stop and the size of each step between values

def totalCounts(data):
    count = 0
    for i in data:
        if i==i:
            count = count+1
    return (count)
def completeCalc(infile, outfile, initial):
    ss = time.time()
    chunks = (10 * 10 ** 6)
    file = pd.read_csv(str(infile), chunksize=(chunks))
    cc = 0
    for chunk in file:
        cc = cc + 1
        arrivalTimes = np.array([], dtype=np.float64)
        df = pd.DataFrame(chunk)
        arrivalTimes = np.append(arrivalTimes, df['Arrival Times'])
        print(totalCounts(df['Arrival Times']))
        print(df['Arrival Times'].iloc[0])
        count1 = 0
        result = cp.ones((int((end - start) / step), 1))
        while count1 < ((end - start) / step):
            st = time.time()
            result[count1] = ZnCalculation(count1, arrivalTimes, initial)
            count1 = count1 + 1
            print('Iteration: ' + str(count1))
            et = time.time()
            print('Iterarion Time: ' + str(et - st) + 'seconds')
        print(result)
        resultCount = 0
        for i in result:
            if i == i:
                resultCount = resultCount + 1
        scaling = result * 10000
        ee = time.time()
        print('Time Elaspsed: '+ str(ee-ss) + ' seconds')
        pd.DataFrame(scaling).to_csv(
            str(outfile) + str(start) + '-' + str(end) + '-' + str(step) + '-' + str(cc) + '.csv', index='Zn2 Values')

completeCalc('corr40050-04-01-00_123micro.csv', 'D:\Research\Helpful scripts\Extractor\Zn2 Results\MXB_1659-29\P40050\P40050-04-01/P40050-04-01',537243111.2524363)