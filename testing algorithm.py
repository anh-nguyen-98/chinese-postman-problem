<<<<<<< HEAD
"""
first algorithm test
author:
"""
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

filename = "graph 1.csv"
with open(filename, 'r') as in_file:
    data = pd.read_csv(filename)
    
G = nx.Graph()
G.add_nodes_from(data.columns[1:])
print(G.nodes)


for row in data.index.array:
    for col in data.columns[1:]:
        data = data.fillna(0)
        if data.iloc[row][col] != 0:
            G.add_edge(data.iloc[row][0], col, weight = data.iloc[row][col])
   
            
#print(data.iloc[0]['B'])           
print(G.edges)

pos = nx.spring_layout(G)  # positions for all nodes

print (pos)
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=6)
plt.axis("off")
plt.show()

#is eulerian graph
=======
"""
first algorithm test
author:
"""
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

import tkinter as tk
from io import BytesIO
from turtle import TurtleScreen, RawTurtle
from PIL import Image, ImageTk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
root = tk.Tk()


filename = "graph 1.csv"
with open(filename, 'r') as in_file:
    data = pd.read_csv(filename)
    
G = nx.Graph()
G.add_nodes_from(data.columns[1:])
print(G.nodes)


for row in data.index.array:
    for col in data.columns[1:]:
        data = data.fillna(0)
        if data.iloc[row][col] != 0:
            G.add_edge(data.iloc[row][0], col, weight = data.iloc[row][col])
   
            
#print(data.iloc[0]['B'])           
print(G.edges)

pos = nx.spring_layout(G)  # positions for all nodes

print (pos)
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=6)
plt.axis("off")
print (G.degree)



def is_eulerian (G):
    degree_list = [val for (node, val) in G.degree()]
    for i in degree_list:
        if i %2 == 1:
            return False
    return True
        
print(is_eulerian(G))
#Get length path: 
def get_length_path (G): 
    total_weight = 0
    for edge in G.edges:
        
        total_weight += G.get_edge_data(edge[0], edge[1])["weight"]
    return total_weight


#step 2: list of odd-deree vertices:
def get_odd_degree_list(G): 
    odd_degree_list = []
    degree_list = [val for (node, val) in G.degree()]
        for i in degree_list:
            if i %2 == 1:
                odd_degree_list.append(i)
     return odd_degree_list
    
    

#step 3:

#odd_degree_list = (A, B, C, D)
#=> 3 ways to pair
#1: A-B, C-D

#2: A-C, B-D

#3: A-D, B-C
    
    
    
#visualize graph with turtle 
x_coordinates = []
y_coordinates = []
for i in pos.keys():
    x_coordinates += [pos[i][0]]
    y_coordinates += [pos[i][1]]
    
print (x_coordinates)


    
    
# Plot graph
figure = Figure(figsize=(5, 5))
subplot = figure.add_subplot(111)
x = np.array(x_coordinates)
y = np.array(y_coordinates)
subplot.plot(x, y)


# Make memory image of graph
invisible_figure_canvas = FigureCanvasTkAgg(figure, root)
buffer = BytesIO()
figure.savefig(buffer, format="png")
buffer.seek(0)


# Open memory as tkinter image
image = Image.open(buffer)
photoImage = ImageTk.PhotoImage(image)
buffer.close()

# Now do our turtle drawing embedded in tkinter
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

screen = TurtleScreen(canvas)
screen._setbgpic(screen._bgpic, photoImage)  # bypass restrictions (protected access)

turtle = RawTurtle(screen, shape='turtle')
turtle.shapesize(4)

def route (turtle, x_coordinates, y_coordinates):
    
    for x, y in zip(x_coordinates, y_coordinates):
        
        turtle.goto(x, y)
        



route(turtle, x_coordinates, y_coordinates)

screen.mainloop()



#plt.show()







>>>>>>> 32afb0c53cff3033ca4400e11461abeb6e3d04a1
