#Program to create dictionary - > form a DAG for all possible combination of Kmer
#https://www.python.org/doc/essays/graphs/

import collections, sys
import csv
import datetime


#USAGE : python par_dfs.py input output min_path_len

# Set limit of recursion stack
x=150000
sys.setrecursionlimit(x)

filename=sys.argv[1]
outname=sys.argv[2]
minlen = int(sys.argv[3])  #min length of path
writefile = open(outname+".findpath","w")




# Read input file
readfile = open(filename,"r")
filedata = readfile.readlines()
readfile.close()
t_line=[]
for every_line in filedata:
       t_line.append(every_line.split("\n"))
    
kmer_size=len(t_line)
#print kmer_size

#.replace("'","").replace("{","").replace("}","").
# Map kmers into integers             
graph = {}
for i in range(kmer_size):
    gval=[]  
    read = t_line[i][0].replace(" ","").split("[")
    numstr2 = read[1].replace("]","")
    numstr2 =  numstr2[1:-1].split(',')
    for ele in numstr2:
        gval.append(ele.replace("'",""))
    graph[read[0]]= gval


start_time = datetime.datetime.now()

#newpaths=[]

def find_all_paths(start, path=[]):
	path = path + [start]	
	#newpaths=[]
	#print "||",path
	if graph.has_key(start):
            for node in graph[start]:
	      if node not in path:
		   if graph.has_key(node):
			find_all_paths(node,path)
		   else: 
		       path_1 = path+[node]
		       if ((len(path_1) > minlen) and (len(path_1) < 700)):
			  writefile.write(str(path_1)+"\n") 
		       
		
for key, value in graph.items():
	find_all_paths(key)
	
end_time = datetime.datetime.now()
print("Time Required:")
print(end_time-start_time)

