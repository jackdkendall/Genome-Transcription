#!/usr/local/bin/python2.7

from sys import argv
script, filename = argv
data = open(filename)

genome_dict = {'t': 1, 'c': 2, 'a': 3, 'g': 4};

amino_dict = {111 : "Phe", 112 : "Phe", 113 : "Leu", 114 : "Leu", \
121 : "Ser", 122 : "Ser", 123 : "Ser", 124 : "Ser", \
131 : "Tyr", 132 : "Tyr", 133 : "STOP", 134 : "STOP", \
141 : "Cys", 142 : "Cys", 143 : "STOP", 144 : "Trp", \
211 : "Leu", 212 : "Leu", 213 : "Leu", 214 : "Leu", \
221 : "Pro", 222 : "Pro", 223 : "Pro", 224 : "Pro", \
231 : "His", 232 : "His", 233 : "Gln", 234 : "Gln", \
241 : "Arg", 242 : "Arg", 243 : "Arg", 244 : "Arg", \
311 : "Ile", 312 : "Ile", 313 : "Ile", 314 : "Met", \
321 : "Thr", 322 : "Thr", 323 : "Thr", 324 : "Thr", \
331 : "Asn", 332 : "Asn", 333 : "Lys", 334 : "Lys", \
341 : "Ser", 342 : "Ser", 343 : "Arg", 344 : "Arg", \
411 : "Val", 412 : "Val", 413 : "Val", 414 : "Val", \
421 : "Ala", 422 : "Ala", 423 : "Ala", 424 : "Ala", \
431 : "Asp", 432 : "Asp", 433 : "Glu", 434 : "Glu", \
441 : "Gly", 442 : "Gly", 443 : "Gly", 444 : "Gly"}

def grouper(seq, n):
	return( [int( ''.join( map( str, seq[i:i + n]))) for i in range( 0, len(seq), n)])

with data as f:
	read = f.read()
	N = list(read.lower())
print "The nucleotide sequence is: ", "\n \n", N, "\n"

M = [(genome_dict[i]) for i in N]
c = len(M) // 3
print "The number of codons in this sequence is: ", c, "\n"

Protein = []

for group in grouper(M, 3):
	print group
	if  group == 133:
		print "\nStop codon hit. Sequence terminated."
		break
	elif  group == 134:
		print "\nStop codon hit. Sequence terminated."
		break
	elif  group == 143:
		print "\nStop codon hit. Sequence terminated."
		break
	else:
		Protein.append(amino_dict[group])

print "\n"
print "This corresponds to a protein primary structure of: \n \n", Protein, "\n"