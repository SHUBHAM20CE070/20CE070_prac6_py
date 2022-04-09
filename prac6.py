#20CE070_Shubham_Panchal
#Prac6_PYTHON


# You are given n words. Some words may repeat. 
# For each word, output its number of occurrences. 
# The output order should correspond with the input order of appearance of the word.
# See the sample input/output for clarification. 

import collections;

a= int(input())
b = collections.OrderedDict()

for i in range(a):
    word = input()
    if word in b:
        b[word] +=1
    else:
        b[word] = 1

print(len(b));

for k,v in b.items():
    print(v,end = " ");