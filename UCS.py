from tabulate import tabulate
            
def UCS(start, goal, searchSpace):
    openList = [(start, 0)] 
    closedList = []
    path = {}
    table_headers = ["Open List","N","Closed List","Goal Test","Successors"]
    table_data =[]
    cost_so_far = {node: float('inf') for node in searchSpace}
    cost_so_far[start] = 0

    while openList:
        openList.sort(key=lambda x: x[1]) 
        temp = openList[:]
        N, cost = openList.pop(0)

        if N not in closedList:
            closedList.append(N)
        current_closed_list = closedList[:]

        if N == goal:
            data = [temp,N,current_closed_list,True ,"-"]
            table_data.append(data)
            break

        children = searchSpace[N]
        for child, edge_cost in children:
            new_cost = cost + edge_cost
            if new_cost < cost_so_far[child]:
                # cost_old = cost_so_far[child]
                cost_so_far[child] = new_cost
                path[child] = N
                openList.append((child, new_cost))
        data = [temp,N,current_closed_list,False ,children]
        table_data.append(data)

    table = tabulate(table_data, headers=table_headers, tablefmt="grid")
    current = N
    path_taken = [current]
    while current != start:
        current = path[current]
        path_taken.append(current)
        path_taken.reverse()
    print(f"Path Taken is : {path_taken}")
    print("Table: ")
    print(table)


start = 'D'
goal = 'R'

searchSpace = {'A':[],
               'B':[['A',2]],
               'C':[['A',1]],
               'D':[['C',8],['E',2],['B',1]],
               'E':[['R',2],['H',8]],
               'F':[['G',2],['C',3]],
               'G':[],
               'H':[['Q',5],['P',7]],
               'P':[['Q',15]],
               'Q':[],
               'R':[['F',1]],
               'S':[['D',3],['E',9],['P',1]]
}

UCS(start,goal,searchSpace)