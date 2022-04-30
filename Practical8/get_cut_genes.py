#get_cut_genes.py
import os
f = open('/Users/yywang/PycharmProjects/pythonProject/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')#the pathway is from my computer, if you want to check it, the pathway of the film needs to be changed
SEQ = {}#save the file in a dictory
for line in f:
        if line.startswith('>'):#find the whole paragraph of a complete sequence
                name=line.replace('>','').split()[0]
                SEQ[name]=''#staart a new string with the name of the string
        else:
                SEQ[name]+=line.replace('\n','').strip()#continue the string of base
# origin link：https://blog.csdn.net/Cccrush/article/details/80112198
content = ""
for keys, values in SEQ.items():
    if str(values).find('GAATTC') >= 0:#find the strings that have GAATTC
        content = content + '\n>'+keys+'              '+str(len(values))+'\n' + str(values)#save it in one place to output it#give the form of fasta
    else:
        continue
print(content)
name = 'cut_genes'
desktop_path = os.path.join(os.path.expanduser('~'),"Desktop/")#find the pathway to the desktop folder
full_path = desktop_path + name + '.fa'
file = open(full_path,'w')
file.write(content)#input the results into the file
file.close()
