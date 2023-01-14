### Prerequisites :

The required dependencies for **SecDATA** are Processor - Intel® Xeon(R) Silver 4215 CPU @ 2.50GHz × 16
Memory – 128 gb
OS - Ubuntu 18.04.5 LTS
python version 3.O <br/>
**SecDATA** is tested to work under Ubuntu 18.04 and the important instructions to run it  are given below : - <br/>

### To start a run : <br/>

Our computational configuration is as follows -
Processor - Intel® Xeon(R) Silver 4215 CPU @ 2.50GHz × 16
Memory – 128 gb
OS - Ubuntu 18.04.5 LTS
python version 2.7



Step 1: python kmer_v1.2.py 21 SRR11771595.fa kmer95.txt

Step 2: python par_dictv2.py kmer95.txt kmer95 20		

Step 3: python par_dfs.py kmer95.dictionary out95 100		

Step 4: python DFS_transcript.py kmer95.txt out95 


Step 5: Required to make proper format for next step
	
cat out95.trancript > out95trancript.fa 

Step 6: javac runtest2.java
	java  runtest2
				[N.B it will generate a file say sorttrans.txt	]
Step 7: sort sorttrans.txt | uniq  >  trans.txt

Step 8: then we have to execute makefasta.java with  trans.txt
it will create a fasta file ( say out95trancript.fa)

Step 9: again we have to validate with blat 
blat Mouse_cDNA_fasta.fa out95trancript.fa blatout95.psl
sed -n '6,$p' blatout95.psl| awk -F'\t' '  $5=="0" {a+=1} $5=="1" {b+=1} END { printf "0= %d\n 1= %d", a,b }'

awk '{ print $10 }' out97.psl | sort | uniq | wc -l
 awk '{ print $10 }' out97.psl | wc -l


awk '{ print $14 }' out97.psl | uniq | wc -l
awk '{ print $14 }' out97.psl | uniq | wc -l
