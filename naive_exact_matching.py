import random

# |p| = x, |t| = y
# Number of possible alignments: y - x + 1
# Greatest possible number of character comparisons: x * (y - x + 1) "worst" case (only matches)
# Least amount of character comparisons: y - x + 1 "best" case (no matches)

def naiveExactMatching(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i + j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences

t = 'ACTGGCGAGTGTTGC'
p = 'TG'
print(naiveExactMatching(p, t))

# Naive exact matching on artifical reads

# Read in genome

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if line[0] != '>':
                genome += line.rstrip()
    return genome

genome = readGenome('phix.fa.1')

# Generate artifical reads

def generateReads(genome, numReads, readLen):
    ''' Generate reads from random positions in the given genome. '''
    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome)-readLen) - 1
        reads.append(genome[start : start+readLen])
    return reads

# 100 reads of length 100

reads = generateReads(genome, 100, 100)

# Count number of reads that match the genome exactly

numMatched = 0
for r in reads:
    matches = naiveExactMatching(r, genome)
    if len(matches) > 0:
        numMatched += 1

print('%d / %d reads matched exactly.' % (numMatched, len(reads)))

# Naive exact matching on real reads

# Read in sequence reads from file

def readFastq(filename):
    seqs = []
    quals = []
    with open(filename) as f:
        while True:
            f.readline()
            seq = f.readline().rstrip()
            f.readline()
            qual = f.readline().rstrip()
            if len(seq) == 0:
                break
            seqs.append(seq)
            quals.append(qual)
    return seqs, quals

phix_reads, _ = readFastq('ERR266411_1.first1000.fastq')

# Helper function

def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

# Count number of phix reads that match the genome

numMatched = 0
n = 0
for r in phix_reads:
    r = r[:30]
    matches = naiveExactMatching(r, genome)
    matches.extend(naiveExactMatching(reverseComplement(r), genome))
    n += 1
    if len(matches) > 0:
        numMatched += 1

print('%d / %d reads matched the genome.' % (numMatched, n))