import re
import os
os.chdir('/Users/13035/IBI1_2020-21/Practical8')
F1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
F2 = open('unknown_function.fa','w')
f=''
z=''
Boole = False
#open the loop
for line in F1:
    if line.startswith('>'):
        if Boole == True:
            # list the name of gene and the long of the gene
            f=f+('>'+b+'     '+str(len(z))+'\n'+z+'\n')
            z=''
            Boole ==False
        if re.findall(r'unknown',line):
            # find the line and list the name of gene
            b=re.findall(r'^>.+?_',line)
            b=b[0]
            b=b[:-1]
            Boole=True
    else:
        if Boole ==True:
            z=z+line.strip()+'\n'
F1.close()
F2.write(f)
F2.close()