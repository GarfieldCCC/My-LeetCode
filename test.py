def find_the_difference(s, t):
    big = s if s.__len__() > t.__len__() else t
    small = s if s.__len__() < t.__len__() else t
    s = "".join(sorted(list(small)))
    t = "".join(sorted(list(big)))
    for i in range(s.__len__() + 1):
        if s[0:i] != t[0:i]:
            return t[i-1]
    return t[-1]


ss = "ae"
tt = "aea"

print(find_the_difference(ss, tt))
