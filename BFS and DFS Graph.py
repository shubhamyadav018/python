BFS of a graph 1:-

def BFSTraversal(adj,n):
    visited=[False]*(n+1)
    result=[]
    for i in range(1,n+1):
        if visited[i]==False:
            storeBFS(i,result,adj,n,visited)
    print(*result)
   



def storeBFS(startNode,result,adj,n,visited):
    visited[startNode]=True
    Q=[startNode]
    while len(Q)>0:
        currNode=Q.pop(0)
        result.append(currNode)
        for n in adj[currNode]:
            if visited[n]==False:
                visited[n]=True
                Q.append(n)


n, m = map(int, input().split())
adj = []
for i in range(n+1): 
    adj.append([])
 
for i in range(m):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

    
BFSTraversal(adj,n)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DFS of a graph:-

def initiateDFS(node, visited, adj, result):
    result.append(node)
    visited[node] = True 
 
    for neighbour in adj[node]:
        if visited[neighbour] == False:
            initiateDFS(neighbour, visited, adj, result)
 
 
def printDFSTraversal(adj, n):
    result = []
    visited = [False] * (n+1) 
 
    for i in range(1,n+1):
        if visited[i] == False:
            initiateDFS(i, visited, adj, result)
    print(*result)
 

n, m = map(int, input().split())
adj = []
for i in range(n+1): 
    adj.append([])

for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
printDFSTraversal(adj, n)
