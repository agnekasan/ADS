complement = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}

def reverseComplement(s):
    t = ''
    for base in s:
        t = complement[base] + t
    return t

print(reverseComplement('ACTGG'))