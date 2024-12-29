import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QGridLayout, QLabel, QTableWidget, QTableWidgetItem, QFrame
from PyQt5.QtGui import QColor
import time
from tabulate import tabulate

def Heuristic_Manhattan(node,goal):
    #Heuristic is manhattan
    #Manhattan -> d(x,y)= |x_goal - x_node| + |y_goal - y_node|
    (x_node,y_node) = node
    (x_goal,y_goal) = goal
    return abs(x_goal - x_node) + abs(y_goal - y_node)

def get_neighbors(searchspace, node):
    (x_node,y_node) = node
    neighbours = []
    # Defining the possible moves (top, bottom, left, right)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in moves:
        row_coordinate, column_coordinate = (x_node + dr),(y_node + dc)
        if 0 <= row_coordinate < len(searchspace) and 0 <= column_coordinate < len(searchspace[0]) and searchspace[row_coordinate][column_coordinate] == 1:
            neighbours.append((row_coordinate, column_coordinate))
    return neighbours

def Astar(start, goal, searchspace, maze_widget):
    cost = 0
    open_list = [(start,Heuristic_Manhattan(start,goal)+cost)]
    closed_list = []
    table_headers = ["Open List", "N", "Closed List", "Goal Test","Successor"]
    table_data = []
    path = {}

    while len(open_list):
        temp = open_list[:]
        open_list.sort(key=lambda x: x[1]) 
        N,astar_value = open_list.pop(0)
        cost = astar_value - Heuristic_Manhattan(N,goal)
        if N not in closed_list and N not in open_list:
            closed_list.append(N)
        
        if N == goal:
            table_data.append([temp, N, closed_list, True, ""])
            break
        
        #Finding the successors of N in the table
        N_neighbours = get_neighbors(searchspace,N)
        children = []
        cost = cost +1
        for node in N_neighbours:
            children.append((node,Heuristic_Manhattan(node,goal)+cost))

        #Adding the childrens to open list carefully
        for child in children:
            (child_coordinate,child_value) = child
            if child_coordinate not in open_list and child_coordinate not in closed_list:
                open_list.append(child)
                path[tuple(child_coordinate)] = N
        table_data.append([list(temp), N, list(closed_list), False, list(children)])

        # Skip changing the color of the start block to yellow
        if N != start:
            maze_widget[N[0]][N[1]].setStyleSheet("background-color: yellow;")
        time.sleep(0.1)  # Add a delay to see the traversal
        QApplication.processEvents()

    path_taken = []
    current = tuple(goal)
    while tuple(current) != tuple(start):
        path_taken.append(tuple(current))
        current = path[tuple(current)]
    path_taken.append(tuple(start))
    path_taken.reverse()
    return table_data, path_taken

class AstarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Astar Maze Solver')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.run_button = QPushButton('Run Astar', self)
        self.run_button.clicked.connect(self.run_Astar)

        self.maze_label = QLabel('Maze:', self)

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)  # Set spacing to zero
        self.grid_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        self.maze_widget = []

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.run_button)
        self.layout.addWidget(self.maze_label)
        self.layout.addLayout(self.grid_layout)

    def create_maze_widget(self, searchspace):
        for i, row in enumerate(searchspace):
            maze_row = []
            for j, block in enumerate(row):
                block_frame = QFrame(self)
                block_frame.setFixedSize(40, 40)
                block_frame.setAutoFillBackground(True)
                if block == 0:
                    block_frame.setStyleSheet("background-color: gray; border: 1px solid black;")
                elif (i, j) == self.start:
                    block_frame.setStyleSheet("background-color: red; border: 1px solid black;")
                elif (i, j) == self.goal:
                    block_frame.setStyleSheet("background-color: green; border: 1px solid black;")
                else:
                    block_frame.setStyleSheet("background-color: white; border: 1px solid black;")
                maze_row.append(block_frame)
                self.grid_layout.addWidget(block_frame, i, j)
            self.maze_widget.append(maze_row)

    def run_Astar(self):
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(1)  # Set spacing to zero
        self.grid_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        self.maze_widget = []
        self.layout.addLayout(self.grid_layout)

        start = (3, 0)
        goal = (1,10)

        searchspace = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
            ]
        
        # searchspace = [
        #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        #     [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        #     [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        #     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # ]

        self.start = start
        self.goal = goal

        self.create_maze_widget(searchspace)

        table_data, path_taken = Astar(start, goal, searchspace, self.maze_widget)

        self.Astar_table = QTableWidget(self)
        table_headers = ["Open List", "N", "Closed List", "Goal Test", "Successor"]
        self.Astar_table.setRowCount(len(table_data))
        self.Astar_table.setColumnCount(len(table_headers))
        self.Astar_table.setHorizontalHeaderLabels(table_headers)

        for i, row in enumerate(table_data):
            for j, item in enumerate(row):
                self.Astar_table.setItem(i, j, QTableWidgetItem(str(item)))

        print("Path followed is: ", path_taken)
        print(tabulate(table_data, table_headers, tablefmt="grid"))

def main():
    app = QApplication(sys.argv)
    window = AstarApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
