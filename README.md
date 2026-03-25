# Artificial Intelligence Lab Programs

This repository contains Python implementations of fundamental Artificial Intelligence concepts, focusing on agent simulations and search algorithms.

## Project Structure

The repository is organized into laboratory exercises, starting with basic agent behaviors and moving toward environment interactions and tree searching.

### Lab 1: Agent Simulations

* **p1.py & p2.py: Simple Reflex Agent**
    * Implements a basic vacuum cleaner agent that operates based on its current percept (location and status).
    * **p1.py** demonstrates a single action based on a static environment.
    * **p2.py** simulates the agent over multiple iterations, updating the environment status from "Dirty" to "Clean" as it moves between locations A and B.

* **p3.py & p4.py: Goal-Based and Rational Agents**
    * **p3.py** provides a functional approach to moving an entity toward a specific goal position.
    * **p4.py** utilizes an Object-Oriented approach with a `RationalAgent` class to encapsulate the state and logic required to reach a goal.

* **p5.py: Grid-Based Vacuum Cleaner Simulation**
    * Simulates a 4x4 room environment represented as a grid where all cells are initially dirty.
    * Features random dirt generation across the grid.
    * Implements a systematic cleaning process and calculates performance metrics.

### Lab 2: Tree Search Algorithms

* **p6.py: Breadth-First Search (BFS)**
    * Implements BFS for a tree structure starting from the root node.
    * Explores all neighboring nodes at the present depth level before moving to the next level using a Queue (FIFO) approach.
    * Output displays the level-order traversal (e.g., 1 2 3 4 5 6 7).

* **p7.py: Depth-First Search (DFS)**
    * Implements DFS for a tree structure starting from the root node.
    * Explores as far as possible along each branch before backtracking using a recursive/Stack (LIFO) approach.
    * Output displays the depth-first traversal (e.g., 1 2 4 5 3 6 7).

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/labspider/ai-lab/blob/main/LICENSE) file for details.