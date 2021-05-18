from xml.dom.minidom import parse
import xml.dom.minidom
import sys
sys.setrecursionlimit(500000)#Open limit
import os
import matplotlib.pyplot as plt
os.chdir("/Users/13035/IBI1_2020-21/Practical14")
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
def dict_founder(terms):
    dict = {}#make a dict
    for term in terms:
        is_a = [child.childNodes[0].data 
        for child in term.getElementsByTagName("is_a")]
        id = term.getElementsByTagName("id")[0].childNodes[0].data
        for father_id in is_a:
            if father_id in dict:
                dict[father_id].append(id)
            else:
                dict[father_id] = [id]
    return dict

def related_gene(terms,molecule):
    gene = []
    for term in terms:
        defstrs = term.getElementsByTagName("defstr")[0]
        id_r = term.getElementsByTagName("id")[0].childNodes[0].data
        #find the related ID
        f = defstrs.childNodes[0].data
        if not molecule.isupper():
            f = f.lower()
        if molecule in f:
            gene.append(id_r)
    return set(gene)
def getall(dict,lists):
    all = []
    for F in lists:
        if F in dict:
            child = dict[F]
            all += child
            all += getall(dict,child)
    return all#To find all child we needed
def counting_the_childnodes(terms,molecular):
    dict = dict_founder(terms)
    match = related_gene(terms,molecular)
    all_childnodes = getall(dict,match)
    num = len(set(all_childnodes))#Remove duplicates
    return num
def pie_chart(x1,x2,x3,x4):
    total = x1 + x2 + x3 + x4
    list = [x1,x2,x3,x4]
    percentage = []
    for i in range(len(list)):
        p = 100*(list[i]/total)
        percentage.append(p)
    labels = 'DNA', 'RNA', 'Protein', 'Carbohydrate'
    sizes = percentage
    plt.title("Child Nodes of 4 macromolecules") 
    plt.pie(sizes,labels=labels,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
    # make a pie chart
DNA = counting_the_childnodes(terms,"DNA")
RNA = counting_the_childnodes(terms,"RNA")
Protein = counting_the_childnodes(terms,"protein")
Carbohydrate = counting_the_childnodes(terms,"carbohydrate")

print("The childNodes number of  DNA-associated terms is: ",DNA)
print("The childNodes number of  RNA-associated terms is: ",RNA)
print("The childNodes number of  protein-associated terms is: ",Protein)
print("The childNodes number of  carbohydrate-associated terms is: ",Carbohydrate)
pie_chart(DNA,RNA,Protein,Carbohydrate)