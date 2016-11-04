


def primitive(n):

    table = { 1 : 1 }
    x = 0 # 96234

    for i in range(1,n+1):

        if table[i+1] == None or table[i+1] > table[i] + 1:
            v[i+1] = v[i] + 1
        if table[i*2] == None or table[i*2] > table[i] * 2:
            v[i*2] = v[i] * 2
        if table[i*3] == None or table[i*3] > table[i] * 3:
            v[i*3] = v[i] * 3

    print table
