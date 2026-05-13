INF = float('inf')

def floydWarshall(dists, n, prevs) -> None:
    for k in range(n):
        for i in range(n):
            for j in range(n):
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
    vertexMapping = dict()
    n, vi = 0, 0

    edgeList = []
    isDirected = False

    with open('input.csv', 'r') as file:
        isDirected = file.readline().strip().split(',')[1].lower() == 'yes'
        file.readline()
        for line in file.readlines():
            # u, v, w = map(int, line.strip().split(','))
            u, v, w = line.strip().split(',')
            w = int(w)

            if u in vertexMapping:
                u = vertexMapping[u]
            else:
                vertexMapping[u] = vi
                vertexMapping[vi] = u
                u = vi
                vi += 1

            if v in vertexMapping:
                v = vertexMapping[v]
            else:
                vertexMapping[v] = vi
                vertexMapping[vi] = v
                v = vi
                vi += 1

            edgeList.append((u, v, w))
            n = max([n, u, v])
        n += 1

    dists = [[INF for _ in range(n)] for _ in range(n)]
    prevs = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
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
        for i in range(n):
            for j in range(n):
                if dists[i][j] != INF:
                    file.write(f'{vertexMapping[i]},{vertexMapping[j]},{dists[i][j]},')
                    path = getPath(prevs, i, j)
                    for node in path[:-1]:
                        file.write(f',{vertexMapping[node]} ->')
                    if path:
                        file.write(f',{vertexMapping[path[-1]]}\n')
                    else:
                        file.write('\n')
                else:
                    file.write(f'{vertexMapping[i]},{vertexMapping[j]},unreachable\n')