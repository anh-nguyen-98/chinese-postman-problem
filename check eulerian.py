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

# positions for all nodes
pos = nx.spring_layout(G)  
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
        if i % 2 == 1:
            return False
    return True
        
print(is_eulerian(G))

#Get length path: 
def get_length_path (G): 
    total_weight = 0
    for edge in G.edges:
        
        total_weight += G.get_edge_data(edge[0], edge[1])["weight"]
    return total_weight


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
turtle.shapesize(1)

def route (x_coordinates, y_coordinates):
    
    for i in range(len(x_coordinates)):
        turtle.pensize(1)
        turtle.pendown()
        turtle.speed(3)
        turtle.goto(int(x_coordinates[i]), int(y_coordinates[i]))
        
route(x_coordinates, y_coordinates)
screen.mainloop()


#plt.show()







