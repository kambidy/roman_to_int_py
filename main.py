def romanToInt(self, s: str) -> int:
    s = s.replace("IV","IIII",-1)
    s=s.replace("IX","VIIII")
    s=s.replace("XL","XXXX")
    s=s.replace("XC","LXXXX")
    s=s.replace("CD","CCCC")
    s=s.replace("CM","DCCCC")
    i = 0
    counter = 0
    while i < len(s):
        if s[i] == 'I':
            counter += 1
        if s[i] == 'V':
            counter += 5
        if s[i] == 'X':
            counter += 10
        if s[i] == 'L':
            counter += 50
        if s[i] == 'C':
            counter += 100
        if s[i] == 'D':
            counter += 500
        if s[i] == 'M':
            counter += 1000
        i += 1
    return counter

