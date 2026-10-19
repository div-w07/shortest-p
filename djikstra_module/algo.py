import json

with open("Map.json", 'r') as f:
    mapp=json.load(f)

def djikstra(mapp,start,end):
    prev={} #stores the previous node for ech node except start
    dist={} #djikstra's tabulation form

    visited=set() #stores the visited nodes to prevent re-entry

    #initialise the table
    for node in mapp:
        dist[node]=float('inf') #initialise all distances to infinity
        prev[node]=None #initialise all previous nodes to None
    
    dist[start]=0
    min_node=start
    while len(visited)<len(mapp):
        for neighbor in mapp[min_node]:
            if neighbor not in visited:
                new_dist=dist[min_node]+mapp[min_node][neighbor]
                if(new_dist<dist[neighbor]):
                    dist[neighbor]=new_dist
                    prev[neighbor]=min_node
        visited.add(min_node)
        if(min_node==end):
            break
        min_node=None
        for node in dist:
            if node not in visited:
                if dist[node]<=dist.get(min_node,float('inf')):
                    min_node=node

    node=end
    print("================================================================================\n================================================================================")
    print(f"The Shortest path from {start} to {end}")
    while node!=start:
        print(node,end="<-")
        node=prev[node]
    print(start)
    print(f"\nTotal Distance: {dist[end]} units")
    print("================================================================================\n================================================================================")
    
djikstra(mapp,"A003","B318")