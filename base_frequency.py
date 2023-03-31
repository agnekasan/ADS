import collections

# read the genome from fasta file

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if line[0] != '>':
                genome += line.rstrip()
    return genome

genome = readGenome('lambda_virus.fa')
print(genome[:300])

# count the frequency of each base

counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for base in genome:
    counts[base] += 1
print(counts)

# shorter version with collections module

print(collections.Counter(genome))