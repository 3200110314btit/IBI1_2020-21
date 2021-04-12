import os
import re
F1 = open(input('the name of the file:'))
output = open('unknown_function.fa','w')
os.chdir('/Users/13035/IBI1_2020-21/Practical8')
# make the dictionary
genetic_code={ 'ATA':'J', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'B', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Z',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'O', 'TAG':'U',
    'TGC':'C', 'TGT':'C', 'TGA':'X', 'TGG':'W'}
F = ''
L = ''
Boolean = False
for line in F1:
    if 'unknown function' in line:
        Boolean = True
        if len(F) != 0:
             output.write(str(len(F))+'\n')
             step = 3
             for i in range(0,len(F),step):
                 L = L + genetic_code[F[i:i+step]]
                 output.write(L)
                 L =''
             n = ''
        output.write('\n'+re.search(r'gene:(\w+)',line).group(1)+'     ')
    elif '>' in line:
        Boolean = False
    else:
        if Boolean == True:
            F = F + line[:-1]
output.write(str(len(F))+'\n')
step = 3
for i in range(0,len(F),step):
    L = L + genetic_code[F[i:i+step]]
    output.write(L)
    L = ''
F1.close()
output.close()
