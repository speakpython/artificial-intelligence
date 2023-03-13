#https://speakpython.codes/artificial-intelligence/2023/03/04/best-first-search.html#graph-relations-and-heuristic

graph_relation = {
    "S": ["A", "B", "C"],
    "A": ["D", "E", "G"],
    "B": ["G"],
    "C": ["G"],
    "D": [""],
    "E": [""],
    "G": [""],
}

heuristic = {
    "S": 8,
    "A": 8,
    "B": 4,
    "C": 3,
    "D": -1,
    "E": -1,
    "G": 0,
}


#https://speakpython.codes/artificial-intelligence/2023/03/04/best-first-search.html#bfs-function

def best_first_search(graph, start, goal, heuristic):
    """
    graph: Dict having Tree Structure.
    start: Starting Node of the Tree.
    goal: Node to Search.
    heuristic: List of heuristic cost.
    """
    que = [(heuristic[start], start)]
    came_from = {}
    came_from[start] = None
    
    while que:
        _, peak_node = heapq.heappop(que)
        
        if peak_node == goal:
            break
            
        for neighbor in graph[peak_node]:
            if neighbor not in came_from:
                heapq.heappush(que, (heuristic[neighbor], neighbor))
                came_from[neighbor] = peak_node
    
    return came_from


#https://speakpython.codes/artificial-intelligence/2023/03/04/best-first-search.html#function-calling

start_node = 'S'
goal_node = 'G'
came_from = best_first_search(graph_relation, start_node, goal_node, heuristic)
print(came_from)


#https://speakpython.codes/artificial-intelligence/2023/03/04/best-first-search.html#backtracking

node = goal_node
path = [node]

while node != start_node:
    node = came_from[node]
    path.append(node)
    
path.reverse()
print("BFS path from",start_node,"to",goal_node,":",path)