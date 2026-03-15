# Artificial Intelligence Lab Programs

This repository contains Python implementations of fundamental Artificial Intelligence concepts, focusing on different types of agents and environment simulations.

## Project Structure

The repository is organized into laboratory exercises, starting with basic agent behaviors and moving toward environment interactions.

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
    * Features random dirt generation (0 for clean, 1 for dirty) across the grid.
    * Implements a systematic cleaning process that visits every cell and activates the vacuum in dirty locations.
    * Includes a performance metric calculation based on the percentage of cells cleaned relative to the total grid size.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/labspider/ai-lab/blob/main/LICENSE) file for details.
