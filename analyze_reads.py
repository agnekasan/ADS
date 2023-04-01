import collections
import matplotlib.pyplot as plt

# read genome and quality from fastq file

def readFastq(filename):
    seqs = []
    quals = []
    with open(filename) as f:
        while True:
            # first line is irrelevant
            f.readline()
            # second line is on read of sequence
            seq = f.readline().rstrip()
            # third line also irrelevant
            f.readline()
            # fourth line is the quality of the sequence
            qual = f.readline().rstrip()
            if len(seq) == 0:
                break
            seqs.append(seq)
            quals.append(qual)
    return seqs, quals

sequences, qualities = readFastq('SRR835775_1.first1000.fastq')
# print(sequences[:3])
# print(qualities[:3])

# quality score histogram

# convert ascii symbols to quality score

def phred33ToQ(qual):
    return ord(qual) - 33

def createHist(qualities):
    hist = [0] * 50
    for qual in qualities:
        for phred in qual:
            q = phred33ToQ(phred)
            hist[q] += 1
    return hist

hist = createHist(qualities)
# print(hist)

# display histogram of qualities

plt.bar(range(len(hist)), hist)
plt.show()

# average GC content plot

# calculate average GC content on each position

def findGCByPosition(reads):
    gc = [0] * 100
    total = [0] * 100

    for read in reads:
        for i in range(len(read)):
            if read[i] == 'C' or read[i] == 'G':
                gc[i] += 1
            total[i] += 1
    
    for i in range(len(gc)):
        if total[i] > 0:
            gc[i] /= float(total[i])
    
    return gc

# display GC content plot

gc = findGCByPosition(sequences)
plt.plot(range(len(gc)), gc)
plt.show()

# distribution of bases

count = collections.Counter()
for seq in sequences:
    count.update(seq)
print(count)