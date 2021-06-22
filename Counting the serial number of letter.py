#WAP to print the letters in decreasing order of frequency
def most_frequent(a):
    a=a.lower()
    d=dict()
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
frequencies=most_frequent('Mississippi')
print(frequencies.items())
