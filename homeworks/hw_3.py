# Do naive exact matching, also check reverse complement
# In case of palindromes, do not count twice
# Input sequence: 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
# Output:
# - sorted list of positions where the input matches the genome
# - number of alignments
# - number of character comparisons

sequence = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
genomeFile = 'chr1.GRCh38.excerpt.fasta'

def readFasta(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

genome = readFasta(genomeFile)

def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

def naiveExactMatching(p, t):
    alignments = 0
    comparisons = 0
    occurrences = []
    reverse = reverseComplement(p)
    for i in range(len(t) - len(p) + 1):
        alignments += 1
        match = True
        for j in range(len(p)):
            comparisons += 1
            if t[i + j] != p[j]:
                comparisons += 1
                if t[i + j] != reverse[j]:
                    match = False
                    break
        if match:
            occurrences.append(i)
    return occurrences, alignments, comparisons

occurrences, alignments, comparisons = naiveExactMatching(sequence, genome)
print('List of occurences: ', occurrences)
print('Number of alignments: ', alignments)
print('Number of character comparisons: ', comparisons)