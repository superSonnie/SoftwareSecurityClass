from collections import deque

n,m,v = map(int, input().split())

graph=[[] for _ in range(n+1)]

visit=[False]*(n+1)

for i in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs_list=[]

def bfs(graph,v,visit):
    queue=deque([v])

    visit[v]=True

    while queue:
        v=queue.popleft()
        bfs_list.append(v)

        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i]=True
        
