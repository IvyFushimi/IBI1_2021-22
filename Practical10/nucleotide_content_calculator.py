#Nucleotide concent calculator

def content(seq):
    """
    INPUT: THE SEQUENCE  both upper and lower cases are ok
    :param seq:
    :return:
    """
    percentageA = str((seq.count('A') + seq.count('a'))/len(seq))#calculate the content of A, including when A is inputed as a
    percentageC = str((seq.count('C') + seq.count('c'))/len(seq))#the same meaning as the line above
    percentageG = str((seq.count('G') + seq.count('g'))/len(seq))
    percentageT = str((seq.count('T') + seq.count('t'))/len(seq))
    print('A:'+percentageA+' C:'+percentageC+' G:'+percentageG+' T:'+percentageT)
    return seq
seq = input('your DNA sequence is :')
content(seq)
'''
example
[in]  your DNA sequence is : ACGTCGATGCTATC
[out] A: 0.21428571428571427 C: 0.2857142857142857 G: 0.21428571428571427 T: 0.2857142857142857
'''
