import sys

k=int(sys.argv[1])
filename=sys.argv[2]
outname=sys.argv[3]


    
    
def count_kmers(seq, k, kmers):
    for i in range(len(seq) - k + 1):
        kmr = seq[i:i + k]

        if kmr in kmers:
            kmers[kmr] += 1

        else:
            kmers[kmr] = 1

kmers = {}

# Put each line of the file into a list (avoid empty lines)
with open(filename) as f:
    lines = [l.strip() for l in f.readlines() if l.strip() != '']

# Find the line indices where a new sequence starts
idx = [i for (i, l) in enumerate(lines) if l[0] == '>']

idx += [len(lines)]

for i in xrange(len(idx) - 1):
    start = idx[i] + 1
    stop = idx[i + 1]
    sequence = ''.join(lines[start:stop])

    count_kmers(sequence, k, kmers)

writefile = open(outname,"w")
for key, value in kmers.items():
	if value >= 15:
      		writefile.write(str(key)+" "+str(value)+"\n")       
                #print key,value





