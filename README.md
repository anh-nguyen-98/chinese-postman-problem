# Chinese Postman Problem 

Chinese Postman Problem aims to find a shortest closed walk of the weighted graph in which each edge is traversed at least once, rather than exactly once. 

* Here is the original problem statement : 

"The (Chinese) Postman Problem, also called Postman Tour or Route Inspection Problem, is a famous problem in Graph Theory: The postman's job is to deliver all of the town's mail using the shortest route possible. In order to do so, he (or she) must pass each street once and then return to the origin."

* Applications: 
  * Node routing problems: Meal delivery, inter-library loans, school-bus routing
  *  Arc routing problems: Waste collection, snow plowing, postal delivery route design

## Installation  
1. Install a Python editor (e.g. Pycharm, Visual Studio Code, Thonny)
2. Clone the project at: 

```
git clone https://github.com/anh-nguyen-98/chinese-postman-problem.git
```
3. Open the project with the existing editor


## Usage 

1. Input your weighted graph's incidence matrix in a .csv file where: 
  - column and row names are vertices
  - cell values are non-negative weight of the respective edges
   
Example:

![graph input](https://github.com/anh-nguyen-98/chinese-postman-problem/blob/main/images/graph.jpg)

2. Run file *shortest_walk_client.py* in your editor 

3. Enter the name of your graph (.csv) in console: 

Example:
![console](https://github.com/anh-nguyen-98/chinese-postman-problem/blob/main/images/input.jpg)


- A Python turtle will visualize the shortest walk on your graph: 
  * Black edge: unvisted edge 
  * Blue edge: edge visited once only 
  * Red edge: edge visited more than once

  a. Example of a being-built tour: 

![being built tour](https://github.com/anh-nguyen-98/chinese-postman-problem/blob/main/images/building%20tour.jpg)


  b. Example of a complete tour: 

![complete tour](https://github.com/anh-nguyen-98/chinese-postman-problem/blob/main/images/complete%20tour.jpg)

## Authors
Nguyen Ba Hoc, Nguyen Hoang Nam Anh 

## Contributing 

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License 


