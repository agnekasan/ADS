def longestCommonPrefix(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]

def match(s1, s2):
    if len(s1) != len(s2):
        return False

    i = 0
    while s1[i] == s2[i]:
        i += 1
        if i >= len(s1):
            return True
    return False

    # for i in range(len(s1)):
    #     if s1[i] != s2[i]:
    #         return False
    # return True

print(match('ACTGGCGAGTGTTGC', 'ACTGGCGAGTGTTGC'))
print(match('ACTGGCGAGTGTTGC', 'ACTGGCGAGTCTTGC'))

print(longestCommonPrefix('ACTGGCGAGTCTTGC', 'ACTGGCTAGTCATGC'))