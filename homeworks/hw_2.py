def readFastq(filename):
    seqs = []
    with open(filename) as f:
        while True:
            f.readline()
            seq = f.readline().rstrip()
            f.readline()
            f.readline()
            if len(seq) == 0:
                break
            seqs.append(seq)
    return seqs

sequences = readFastq('ERR037900_1.first1000.fastq')

# calculate the ratio of faulty bases on each position

def findNByPos(reads):
    n = [0] * 100
    total = [0] * 100

    for read in reads:
        for i in range(len(read)):
            if read[i] == 'N':
                n[i] += 1 
            total[i] += 1
    
    for i in range(len(n)):
        if total[i] > 0:
            n[i] /= float(total[i])

    return n

ns = findNByPos(sequences)

# Finding the position which has the most faulty reads

def findFaultySeqPos(ns):
    faulty = ns.index(max(ns))
    return faulty

print(findFaultySeqPos(ns))