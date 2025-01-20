# Traveling Salesman Problem Solver using Genetic Algorithm

A Python implementation of a Genetic Algorithm to solve the Traveling Salesman Problem (TSP). This program finds an optimal or near-optimal solution for visiting a set of cities exactly once and returning to the starting city, minimizing the total distance traveled.

## 🌟 Features

- Interactive command-line interface for parameter input
- Real-time visualization of the best route using matplotlib
- Configurable genetic algorithm parameters
- Object-oriented implementation of cities and routes
- Elitism preservation for better convergence

## 🚀 Getting Started

### Prerequisites

The program requires Python 3.x and the following libraries:
```bash
pip install matplotlib
```

### Usage

Run the program using:
```bash
python tsp_solver.py
```

You will be prompted to enter:
- Number of cities
- Population size
- Number of generations
- Mutation rate (recommended: 0.01)

## 🧬 Algorithm Structure

### 1. Data Model

#### `Ville` Class
Represents a city with x and y coordinates and methods to:
- Calculate Euclidean distance between cities
- String representation for debugging

### 2. Solution Representation

Each solution (individual) is represented as a permutation of cities, with helper functions:
- `creer_parcours()`: Creates random route permutations
- `longueur_parcours()`: Calculates total route distance

### 3. Genetic Algorithm Components

#### Population Initialization
- `generer_population_initiale()`: Creates initial random population

#### Fitness Evaluation
- `evaluer_population()`: Evaluates and sorts population by route distance

#### Selection
- `selection_par_tournoi()`: Tournament selection for parent choice

#### Crossover
- `crossover_ordonne()`: Order Crossover (OX) operator
  - Preserves order and position of some cities from one parent
  - Fills remaining positions with cities from second parent

#### Mutation
- `mutation_echange()`: Swap mutation operator
  - Randomly exchanges pairs of cities
  - Controlled by mutation rate parameter

#### Generation Evolution
- `nouvelle_generation()`: Creates new population through:
  - Elitism preservation
  - Parent selection
  - Crossover
  - Mutation

### 4. Visualization

- Real-time plotting of best route using matplotlib
- Updates each generation with:
  - Current generation number
  - Best distance found
  - Visual representation of route

## 📊 Performance

The algorithm's performance depends on:
- Number of cities (problem size)
- Population size
- Number of generations
- Mutation rate

Recommended parameters:
- Population size: 50-200
- Generations: 100-1000
- Mutation rate: 0.01

## 🔍 Implementation Details

### Key Features

1. **Elitism**
   - Best solutions preserved across generations
   - Prevents loss of good solutions

2. **Tournament Selection**
   - Efficient parent selection method
   - Maintains population diversity

3. **Order Crossover**
   - Specialized for permutation problems
   - Preserves city order relationships

4. **Adaptive Visualization**
   - Real-time route display
   - Progress monitoring capabilities

## 🤝 Contributing

Feel free to:
- Open issues
- Submit pull requests
- Suggest improvements
- Report bugs

## 📝 License

This project is open source and available under the MIT License.

## 🔗 References

- [Genetic Algorithms Overview](https://en.wikipedia.org/wiki/Genetic_algorithm)
- [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
- [Order Crossover Operator](https://www.researchgate.net/publication/220285784_The_Order_Crossover_Operator)
