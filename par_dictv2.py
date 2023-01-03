#Program to create dictionary - > form a DAG for all possible combination of Kmer#

import collections, sys
import csv
import datetime
import multiprocessing

#USAGE : python par_dict.py input output overlap_len

# Set limit of recursion stack
x=150000
sys.setrecursionlimit(x)

filename = sys.argv[1]
outname = sys.argv[2]
overlap = int(sys.argv[3])  #length of substring overlap


dictfile = open(outname+".dictionary","w")
dictfile.close()



# Read input file
readfile = open(filename,"r")
filedata = readfile.readlines()
readfile.close()
t_line=[]
for every_line in filedata:
       t_line.append(every_line.split())    
kmer_size=len(t_line)


# Map kmers into integers             
kmer=[]
for i in range(kmer_size):
    read = t_line[i]
    c=i+1
    listd= [str(c),read[0]]
    kmer.append(listd)
#print(kmer)

start_time = datetime.datetime.now()


# Create Adjacency List for overlapping kmers using dictionary data structure
graph=dict()

def call(k): 
    gval=[]
    substr1 = kmer[k][1]      # start value
    numstr1= kmer[k][0]
    for j in range(kmer_size):
        if k!=j :         
            substr2 = kmer[j][1]
            numstr2= kmer[j][0]
	    #if v1.endswith(v2[:n]):
            if substr1.endswith(substr2[:overlap]):
                        #print(numstr1,substr1,numstr2,substr2)
                        if numstr2 not in gval and numstr1!=numstr2:
				gval.append(numstr2)
			if len(gval)!=0:
     				graph[numstr1]= gval
    if graph:
    	with open(outname+".dictionary", 'a+') as f:
		for key, value in graph.items():
      			f.write(str(key)+" "+str(value)+"\n")  
	f.close()
    """			
    if graph:
    	with open(outname+".dictionary", 'a+') as f:
		f.write(str(graph)+"\n")
    	f.close() 
    """




for i in range(kmer_size):
	process = multiprocessing.Process(target = call, args = (i, ))
        process.start()
process.join()

end_time = datetime.datetime.now()
print("Time Required:")
print(end_time-start_time)

