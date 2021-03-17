import matplotlib.pyplot as plt
import numpy as np
#firstly,import the numpy and matplotlib.pyplot
gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
exon_counts=np.array([51,1142,42,216,25,650,32533,57,1,523])
#make two lists
AV_exon_length=gene_lengths/exon_counts
AV_exon_length.sort()
#sort the data of AV_exon_length and print
print("A list of sorted values for the average exon length is"+str(AV_exon_length))
plt.boxplot(AV_exon_length,vert=False,whis=2,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False,boxprops={'color':'blue','facecolor':'purple'})
plt.title('AV_exon_length boxplot')
plt.show()

