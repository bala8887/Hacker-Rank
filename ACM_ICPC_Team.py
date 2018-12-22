#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    max=0;
    tmp_max=0;total=0;
    #return topic;
    for i in range(len(topic[0:])):
        for j in range(i+1,len(topic[0:])):
            #tmp_max='{0:b}'.format(int(topic[i])) | '{0:b}'.format(int(topic[j]));
            #tmp_max=str('{0:b}'.format(topic[i]) | '{0:b}'.format(topic[j])).count('1');
            #print (topic[i],topic[j])
            tmp_max=sum([1 for k in range(len(topic[i])) if (topic[i][k]=='1' or topic[j][k]=='1')]);
            #print (range(len(topic[i])));
            #print (tmp_max);
            if tmp_max>max:
                total=0;
                max=tmp_max;
            else:
                if tmp_max==max:
                    total+=1;
                    print (topic[i],topic[j]);
    return ([max,total+1])
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

