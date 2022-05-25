from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
from collections import Counter
import xml.etree.ElementTree



#read the xml file
tree = xml.dom.minidom.parse('go_obo(1).xml')
collection = tree.documentElement
terms = collection.getElementsByTagName('term')#find all the term elemrnts
root = tree.documentElement
term_list=root.getElementsByTagName("term")# the list for all terms.
# count_terms = terms.length#count the total number of terms
# print(count_terms)
#
#find the total number of the'is_a' and the distribution
total_dic={}
for term in term_list:
    node=[]
    for i in term.getElementsByTagName('is_a'):
        node.append(i.childNodes[0].data)
    id_list= term.getElementsByTagName('id')[0].childNodes[0].data
# create total_lic and add the childnode
    for x in node:
        if x in total_dic:
            total_dic[x].append(id_list)
        else:
            total_dic[x]=[id_list]
def add(x):# function 'add' can add the childnodes into the list of parent node, and calculate the lengh of the list
    for i in x:
        if i not in number_list:
            number_list.append(i)
            if i in total_dic:
                add(total_dic[i])
    return len(number_list)
total_list=[]
for term in term_list:
    total_number=0
    id_list=term.getElementsByTagName('id')[0].childNodes[0].data
    childnodes=0
    number_list=[]
    if id_list in total_dic:
        childnodes=add(total_dic[id_list])
    total_list.append(childnodes)
total_number=sum(total_list)#calculate the total number
plt.boxplot(total_list)
plt.ylabel('the number of terms')
plt.xlabel('the number of childnodes')
plt.title('The distribution of child nodes across all terms')
plt.show()

#  translation part
translation=[]
for term in term_list:
    translation_number=0
    if 'translation' in term.getElementsByTagName('defstr')[0].childNodes[0].data:
        id_list=term.getElementsByTagName('id')[0].childNodes[0].data
        if id_list in total_dic:
            childnodes=add(total_dic[id_list])
        translation.append(childnodes)#calculate the total number of childnodes
plt.boxplot(translation)
plt.ylabel('the number of terms')
plt.xlabel('the number of childnodes for translation')
plt.title('The distribution of child nodes across all terms for translation')
plt.show()

#compare the translation average with the total average
average_translation = sum(translation)/len(translation)
all_average = sum(total_list)/len(total_list)
print('average nodes for translation:', average_translation)
print('all average nodes:', all_average)
if average_translation > all_average:
    print('the ‘translation’ terms contain, on average, a greater number of child nodes than the overall Gene Ontology')
if average_translation < all_average:
    print('the ‘translation’ terms contain, on average, a smaller number of child nodes than the overall Gene Ontology')
