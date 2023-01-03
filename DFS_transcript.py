#Program to find transcript#

import numpy as np  
import collections, sys
import csv
import operator
from collections import defaultdict
from collections import deque
from thread import start_new_thread
from time import sleep
import time

#USAGE : python DAG_findallpath_thread.py input1 input2(o/p of dag without extension) --> command same as DAG_findpath_thread.py

kmer_file=sys.argv[1]  # kmer.txt input1 
out_file=sys.argv[2]  # dag.findpath input2
path_file=sys.argv[2]+".findpath"  # file.findpath input2

writefile = open(out_file+".trancript","w")

start_time = time.time()

# Read input file
readfile = open(kmer_file,"r")
filedata = readfile.readlines()
readfile.close()
k_line=[]
for every_line in filedata:
       k_line.append(every_line.split())
    
kmer_size=len(k_line)

# Map kmers into integers             
kmer=[]
for i in range(kmer_size):
    read = k_line[i]
    c=i+1
    list= [str(c),read[0]]
    kmer.append(list)

readfile = open(path_file,"r")
filedata = readfile.readlines()
readfile.close()
path=[]
for every_path in filedata:
       path.append(every_path.split())

path_size=len(path)
tran_list=[]
for i in range(path_size):
    row = str(path[i]).replace("[","").replace("]","").replace("'","").replace(" ","").replace(",","")
    row = row.split("\"\"")
    tran = []
    for ele in row:
	ele= ele.replace("\"","")
	for i in range(kmer_size):
	   if ele == kmer[i][0] :
	   	tran.append(kmer[i][1])		
    tran_list.append(tran)

def merge(s1, s2):
    i = 0
    while not s2.startswith(s1[i:]):
        i += 1
    return s1[:i] + s2

for i in range(len(tran_list)):
     strA=tran_list[i][0]
     for j in range(len(tran_list[i])-1):
		strB = tran_list[i][j+1]
		strA = merge(strA,strB)
     writefile.write(">dag_trans_"+str(i)+"\n"+strA+"\n")   	
writefile.close()
