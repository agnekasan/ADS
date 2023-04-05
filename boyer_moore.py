def z_array(s):
    assert len(s) > 1
    z = [len(s)] + [0] * (len(s)-1)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            z[i] += 1
        else:
            break
    l, r = 0, 0
    if z[1] > 0:
        l, r = 1, z[1]
    for k in range(2, len(s)):
        assert z[k] == 0
        if k > r:
            for i in range(k, len(s)):
                if s[i] == s[i-k]:
                    z[k] += 1
                else:
                    break
            l, r = k, k + z[k] - 1
        else:
            nbeta = r - k + 1
            zkp = z[k - l]
            if nbeta > zkp:
                z[k] = zkp
            else:
                nmatch = 0
                for i in range(r+1, len(s)):
                    # s[i] == s[i - r] ?
                    if s[i] == s[i - k]:
                        nmatch += 1
                    else:
                        break
                # l = k + 1 ?
                l, r = k, r + nmatch
                z[k] = r - k + 1
    return z

print(z_array('aabaabcaabxaacaabaaz'))