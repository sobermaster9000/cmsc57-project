INF = float("inf")


def floydWarshall(dists, n):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dists[i][k] != INF and dists[k][j] != INF:
                    dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])


if __name__ == "__main__":
    edgeList = []
    n = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            u, v, w = map(int, line.split())
            edgeList.append((u, v, w))
            n = max([n, u, v])

    dists = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for u, v, w in edgeList:
        dists[u][v] = dists[v][u] = w

    floydWarshall(dists, n)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"distance from {i} to {j}: {dists[i][j]}")
