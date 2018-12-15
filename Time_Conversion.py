#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    timeList=s.split(':');
    arg_1=timeList[0];
    arg_2=timeList[1];
    arg_3=timeList[2];
    arg_4=s[-2:];
    
    if int(arg_1)<12:
        if arg_4=='PM':
            arg_1=str(int(arg_1)+12);
    
    if (arg_4=='AM'):
        if (int(arg_1)==12):
            arg_1='00';
    
    final_time=arg_1+':'+arg_2+':'+arg_3[0:2];
    return final_time;


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

