import re 
#import
genecode = {'ATA':'J','ATC':'I','ATT':'I','ATG':'M',
'ACA':'T','ACC':'T','ACG':'T','ACT':'T','AAC':'B',
'AAT':'N','AAA':'K','AAG':'K','AGC':'S','AGT':'S',
'AGA':'R','AGG':'R','CTA':'L','CTC':'L','CTG':'L',
'CCA':'P','CCC':'P','CCG':'P','CCT':'P','CTT':'L',
'CAC':'H','CAT':'H','CAA':'Q','CAG':'Z',
'CGA':'R','CGC':'R','CGG':'R','CGT':'R',
'GTA':'V','GTC':'V','GTG':'V','GTT':'V',
'GCA':'A','GCC':'A','GCG':'A','GCT':'A',
'GAC':'D','GAT':'D','GAA':'E','GAG':'E',
'GGA':'G','GGC':'G','GGG':'G','GGT':'G',
'TCA':'S','TCC':'S','TCG':'S','TCT':'S',
'TTC':'F','TTT':'F','TTA':'L','TTG':'L',
'TAC':'Y','TAT':'Y','TAA':'O','TAG':'U',
'TGC':'C','TGT':'C','TGA':'X','TGG':'W'}
#give a dic
seq = 'ATGCGACTACGATCGAGGGCC'
#make a seq
dict()
S = 'the genecode is '
#use for in range to make a circle
for i in range(0,len(seq),3):
    S = S+genecode[seq[i:i+3]]
print(S)
