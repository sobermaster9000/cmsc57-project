INF = float('inf')

def floydWarshall(dists, n, prevs) -> None:
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dists[i][k] + dists[k][j] < dists[i][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
                    prevs[i][j] = prevs[k][j]

def getPath(prevs, u, v) -> list[int]:
    if prevs[u][v] is None:
        return []
    path = [v]
    while u != v:
        v = prevs[u][v]
        path.append(v)
    return path[::-1]

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
        prevs[i][i] = i
    for u, v, w in edgeList:
        dists[u][v] = w
        prevs[u][v] = u
        if not isDirected:
            dists[v][u] = w
            prevs[v][u] = v

    floydWarshall(dists, n, prevs)

    with open('output.csv', 'w') as file:
        file.write('from,to,shortest distance,,path\n')
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dists[i][j] != INF:
                    file.write(f'{i},{j},{dists[i][j]},')
                    path = getPath(prevs, i, j)
                    for node in path[:-1]:
                        file.write(f',{node} ->')
                    if path:
                        file.write(f',{path[-1]}\n')
                    else:
                        file.write('\n')
                else:
                    file.write(f'{i},{j},unreachable\n')