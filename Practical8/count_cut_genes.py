#count_cut_genes.py
'''
many steps are repeated so the same pseudocode will not be marked
'''
import os

f = open('/Users/yywang/PycharmProjects/pythonProject/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')#if you want to run it remember to change the pathway of the sequence
SEQ = {}
for line in f:
        if line.startswith('>'):
                name=line.replace('>','').split()[0]
                SEQ[name]=''
        else:
                SEQ[name]+=line.replace('\n','').strip()
# origin link：https://blog.csdn.net/Cccrush/article/details/80112198
content = ""
for keys, values in SEQ.items():
    if str(values).find('GAATTC') >= 0:
        n = str(values).count('GAATTC')
        content = content + '\n>'+keys+'              '+str(n)+'\n' + str(values)#the n is rewrite as str(n) to fit the format
    else:
        continue
name = input('the name of the file is:')#give the name
desktop_path = os.path.join(os.path.expanduser('~'),"Desktop/")#get the pathway of the desktop to save the file to it
full_path = desktop_path + name + '.fa'#code the form of the fullpath to use it
file = open(full_path,'w')
file.write(content)#input the results into the file
file.close()
