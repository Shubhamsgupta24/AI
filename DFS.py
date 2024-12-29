from tabulate import tabulate

def DFS(start,goal,searchspace):
    open_list = [start]
    closed_list=[]
    table_headers = ["Open List", "N", "Closed List", "Goal Test","Successor"]
    table_data = []
    path = {}
    while open_list:
        temp = open_list[:]
        N = open_list.pop(0)
        if N not in closed_list:
            closed_list.append(N)
        current_closedList = closed_list[:]

        if(N==goal):
            data = [temp, N, closed_list, True, "-"]
            table_data.append(data)
            break
            
        
        else:
            children = searchspace[N]
            for i in range(len(children)-1,-1,-1):
                child=children[i]
                if(child not in open_list and child not in closed_list):
                    open_list.insert(0,child)
                    path[child]=N

        data = [temp , N , current_closedList , False , children]
        table_data.append(data)
    table = tabulate(table_data, headers=table_headers, tablefmt="grid")
    path_taken= []
    current = goal
    while current!=start:
        path_taken.append(current)
        current = path[current]
    path_taken.append(start)
    path_taken.reverse()
    print(f"Path taken is {path_taken}")
    print("Table: ")
    print(table)


start='h'
goal='f'

searchspace = {'a':['h','c','b'],
               'b':['a','d','f'],
               'c':['e','d','a','h'],
               'd':['c','e','g','f','b'],
               'e':['g','d','c'],
               'f':['d','g','b'],
               'g':['e','f','d'],
               'h':['c','a']}



DFS(start,goal,searchspace)