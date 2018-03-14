import sys

def lg(n, b):
    approx = 2
    while n != int((b ** approx)):
        approx += 0.001
    return (approx)

def Four_Russians(a_decimal1,b_rows,n):

    Russian = []
    FourRussians = []
    for zero in range(n):
        zerolist = []
        for i in range(n):
            zerolist.append(0)
        Russian.append(zerolist)
        FourRussians.append(zerolist)

    for u in range(0, len(b_rows)):
        rs = []
        for zero in range(2 ** parts):
            zerolist = []
            for i in range(n):
                zerolist.append(0)
            rs.append(zerolist)
        bp = 1
        k = 0
        for j in range(1, 2 ** parts):
            for l in range(0, n):
                if rs[j - 2 ** k][l] == 0 and b_rows[u][-(k+1)][l] == 0:
                    rs[j][l] = 0
                if rs[j - 2 ** k][l] == 1 or b_rows[u][-(k+1)][l] == 1:
                    rs[j][l] = 1
            if (bp == 1):
                bp = j + 1
                k = k + 1
            else:
                bp = bp - 1

        for count in range(n):
            Russian[count] = rs[int(a_decimal1[u][count], 2)]
        for o in range(n):
            for l in range(n):
                if Russian[o][l] == 1:
                    FourRussians[o][l] = 1
    return FourRussians


if len(sys.argv) > 2:
    first = sys.argv[1]
    second = sys.argv[2]
    a = []
    b = []

    with open(first) as graph_input:

        for size, line in enumerate(graph_input):
            n = + size + 1
            nodes = [int(x) for x in line.split(',')]
            a.append(nodes)
        m = lg(n,2)



        parts = round(m)
        k = parts * n
        seperatedArrayByColumns1 = [row[i:i + parts] for i in range(0, n, parts) for row in a]

        for go in seperatedArrayByColumns1:
            while len(go) < parts:
                go.append(0)

        A = []
        for i in range(0, len(seperatedArrayByColumns1), n):
            A.append(seperatedArrayByColumns1[i:i + n])


    sec = []
    with open(second) as graph1_input:

        for line1 in graph1_input:

            nodes = [int(x) for x in line1.split(',')]
            sec.append(nodes)
            line1.rstrip()
            for p in line1.split(","):

                b.append(int(p))


        seperatedArrayByRows = [b[i:i + k] for i in range(0, len(b), k)]
        for go in seperatedArrayByRows:
            while len(go) < k:
                go.append(0)






        seperatedArrayByRows1 = []
        for i in range(0,len(seperatedArrayByRows)):
            for j in range(0,k,n):
                seperatedArrayByRows1.append(seperatedArrayByRows[i][j:j+n])

        B = []

        for i in range(0, len(seperatedArrayByRows1), parts):
            B.append(seperatedArrayByRows1[i:i + parts])

    A_decimal = []
    for col in A:
        for i in range(n):
            go = ''
            for j in range(parts):
                go = go + str(col[i][j])
            A_decimal.append(go)

    A_decimal1 = [A_decimal[i:i+n] for i in range(0, len(A_decimal), n)]


    FourRus = Four_Russians(A_decimal1,B,n)
    #print(FourRus)


    for i in range(n):
        #print(*FourRus[i], end=",")
        # WORKS KIND OF print(int("".join(str(x) for x in FourRus[i])))

        print (*FourRus[i], sep=",")






















elif len(sys.argv) == 2:


    graph_input1 = sys.argv[1]
    counter = 0
    graph = {}
    with open(graph_input1) as graph_input:
        for line in graph_input:
            parts = line.split()
            counter += 1

            if len(parts) == 1:
                n = int(parts[0])
                graph[n] = []
            else:
                [n1, n2] = [int(x) for x in parts]
                if n1 not in graph:
                    graph[n1] = []
                if n2 not in graph:

                    graph[n2] = []
                graph[n1].append(n2)

    positions = []

    visited = [False for k in graph.keys()]

    def dfs(g, node, positions, visited):
        visited[node] = True
        for v in g[node]:
            if not visited[v]:
                dfs(g, v, positions, visited)
        positions.insert(0, node)


    dfs(graph, 0, positions, visited)
    go = [graph[i] for i in graph.keys()]

    binary_transform = []
    for i in range(len(go)):
        zerolist=[]
        for j in range(len(go)):
            zerolist.append(0)
        binary_transform.append(zerolist)

    for i in range(len(go)):
        if go[i] == []:
            continue
        for j in range(len(go[i])):

            binary_transform[i][go[i][j]] = 1


    for i in range(len(binary_transform)):
        for j in range(len(binary_transform)):
            if i == j:
                binary_transform[i][j] = 1



    m = lg(len(binary_transform), 2)

    n=len(binary_transform)
    parts = round(m)



    B = [binary_transform[i:i + parts] for i in range(0, len(binary_transform), parts)]

    for go in B:


        while len(go) < parts:
            zerolist = []
            for i in range(n):
                zerolist.append(0)

            go.append(zerolist)

    A = [[row[i:i+parts] for row in binary_transform] for i in range(0, len(binary_transform), parts)]

    #for go in seperatedArrayByColumns1:
        #while len(go) < parts:
            #go.append(0)

    for col in A:
        for i in range(n):
            while len(col[i]) < parts:
                if len(col[i]) < parts:

                    col[i].append(0)




    A_decimal = []
    for col in A:
        for i in range(n):
            go = ''
            for j in range(parts):
                go = go + str(col[i][j])
            A_decimal.append(go)


    A_decimal1 = [A_decimal[i:i+n] for i in range(0, len(A_decimal), n)]



    for i in range(n):


        B = [binary_transform[i:i + parts] for i in range(0, len(binary_transform), parts)]
        for go in B:

            while len(go) < parts:
                zerolist = []
                for i in range(n):
                    zerolist.append(0)

                go.append(zerolist)
        A = [[row[i:i + parts] for row in binary_transform] for i in range(0, len(binary_transform), parts)]
        for col in A:
            for i in range(n):
                while len(col[i]) < parts:
                    if len(col[i]) < parts:
                        col[i].append(0)
        A_decimal = []
        for col in A:
            for i in range(n):
                go = ''
                for j in range(parts):
                    go = go + str(col[i][j])
                A_decimal.append(go)


        A_decimal1 = [A_decimal[i:i + n] for i in range(0, len(A_decimal), n)]
        binary_transform = Four_Russians(A_decimal1, B, n)





    for i in range(n):
        for j in range(n):
            if binary_transform[i][j] == 1:
                print(i, j)











else:
    # print (sys.argv[0])
    print("Please enter arguments to make the Four Russians work properly")
    print ("Try again")



