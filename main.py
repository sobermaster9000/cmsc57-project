INF = float('inf')

def floydWarshall(dists, n, prevs) -> None:
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dists[i][k] != INF and dists[k][j] != INF and dists[i][k] + dists[k][j] < dists[i][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
                    # do something to store previous

def getPath(dists, prevs, u, v) -> list[int]:
    # reconstruct path from u to v and return it as a list
    return [1, 2, 3] # test

if __name__ == '__main__':
    edgeList = []
    n = 0
    isDirected = False
    with open('input.csv', 'r') as file:
        isDirected = file.readline().strip()[1].lower() == 'yes'
        file.readline()
        for line in file.readlines():
            u, v, w = map(int, line.strip().split(','))
            edgeList.append((u, v, w))
            n = max([n, u, v])

    dists = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    prevs = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        dists[i][i] = 0
    for u, v, w in edgeList:
        dists[u][v] = w
        if not isDirected:
            dists[v][u] = w

    floydWarshall(dists, n, prevs)

    with open('output.csv', 'w') as file:
        file.write('from,to,distance,path\n')
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dists[i][j] != INF:
                    file.write(f'{i},{j},{dists[i][j]}')
                    path = getPath(dists, prevs, i, j)
                    for node in path[:-1]:
                        file.write(f',{node} ->')
                    file.write(f',{path[-1]}\n')
                else:
                    file.write(f'{i},{j},unreachable,---\n')