from collections import deque

n,m,v = map(int, input().split())

graph=[[] for _ in range(n+1)]

visit=[False]*(n+1)

for i in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_list=[]
def dfs(graph,v,visit):
    visit[v]=True
    dfs_list.append(v)

    for i in graph[v]:
        if not visit[i]:
            dfs(graph,i,visit)
