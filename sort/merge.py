def merge(a,b):
    c = []

    i = 0
    j = 0
    
    for t in range(len(a) + len(b)):
        if i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1
        elif i == len(a) and j < len(b):
            c.append(b[j])
            j = j + 1
        elif i < len(a) and j == len(b):
            c.append(a[i])
            i = i + 1   

    return c