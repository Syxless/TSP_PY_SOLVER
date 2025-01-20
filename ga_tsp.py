import random
import math
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. Data Modeling
# ---------------------------------------------------------------------------

class City:
    """
    Represents a city with x and y coordinates.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        """
        Calculates the Euclidean distance between this city and another city.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self):
        """
        String representation for easier debugging.
        """
        return f"({self.x}, {self.y})"

# ---------------------------------------------------------------------------
# 2. Solution Representation (an individual = a tour = permutation of cities)
# ---------------------------------------------------------------------------

def create_tour(cities):
    """
    Creates a random permutation of the list of cities.
    """
    tour = cities[:]
    random.shuffle(tour)
    return tour

def tour_length(tour):
    """
    Calculates the total distance of a tour (sum of distances
    between successive cities, including the return to the starting point).
    """
    total_distance = 0.0
    for i in range(len(tour)):
        current_city = tour[i]
        next_city = tour[(i + 1) % len(tour)]
        total_distance += current_city.distance(next_city)
    return total_distance

# ---------------------------------------------------------------------------
# 3. Genetic Algorithm
# ---------------------------------------------------------------------------

# 3.1 Population Initialization
def generate_initial_population(pop_size, cities):
    """
    Generates an initial population of size `pop_size`.
    Each individual is a possible tour (a permutation of cities).
    """
    population = []
    for _ in range(pop_size):
        population.append(create_tour(cities))
    return population

# 3.2 Evaluation (fitness)
def evaluate_population(population):
    """
    Returns a list of tuples (tour, total_distance),
    sorted by increasing distance (best first).
    """
    scores = []
    for individual in population:
        dist = tour_length(individual)
        scores.append((individual, dist))
    scores.sort(key=lambda x: x[1])
    return scores

# 3.3 Selection
def tournament_selection(evaluated_pop, tournament_size=3):
    """
    Tournament selection: randomly selects `tournament_size` individuals
    and chooses the best among them.
    """
    selected = random.sample(evaluated_pop, tournament_size)
    selected.sort(key=lambda x: x[1])
    return selected[0][0]  # Returns the individual (not the distance)

# 3.4 Crossover
def ordered_crossover(parent1, parent2):
    """
    Order Crossover (OX) for two permutations.
    This method maintains the order of city appearances.
    """
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    position = end
    for city in parent2:
        if city not in child:
            if position >= size:
                position = 0
            child[position] = city
            position += 1
    return child

# 3.5 Mutation
def swap_mutation(individual, mutation_rate=0.01):
    """
    Mutation by randomly swapping two cities in the tour.
    """
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]
    return individual

# 3.6 New Population Generation
def new_generation(evaluated_pop, pop_size, mutation_rate=0.01, tournament_size=3):
    """
    Creates the new population by:
      - selecting two parents,
      - performing crossover,
      - mutating the child,
      - repeating until the population is filled.
    """
    new_pop = []
    elite_size = 2
    for i in range(elite_size):
        new_pop.append(evaluated_pop[i][0])
    while len(new_pop) < pop_size:
        parent1 = tournament_selection(evaluated_pop, tournament_size)
        parent2 = tournament_selection(evaluated_pop, tournament_size)
        child = ordered_crossover(parent1, parent2)
        child = swap_mutation(child, mutation_rate)
        new_pop.append(child)
    return new_pop

# ---------------------------------------------------------------------------
# 4. Visualization
# ---------------------------------------------------------------------------

def plot_tour(tour, generation, best_distance):
    """
    Plots the tour (city visit order) on a graph.
    """
    plt.clf()
    xs = [city.x for city in tour]
    ys = [city.y for city in tour]
    xs.append(tour[0].x)
    ys.append(tour[0].y)
    plt.plot(xs, ys, marker='o', linestyle='-')
    plt.title(f"Generation: {generation} | Distance: {best_distance:.2f}")
    plt.draw()
    plt.pause(0.001)

# ---------------------------------------------------------------------------
# 5. Main Program
# ---------------------------------------------------------------------------

def main():
    num_cities = int(input("Number of cities: "))
    pop_size = int(input("Population size: "))
    num_generations = int(input("Number of generations: "))
    mutation_rate = float(input("Mutation rate (0.01 recommended): "))
    width, height = 100, 100
    cities = [City(random.uniform(0, width), random.uniform(0, height)) for _ in range(num_cities)]
    population = generate_initial_population(pop_size, cities)
    plt.ion()
    plt.figure(figsize=(6, 6))
    best_global_distance = float('inf')
    best_global_tour = None
    for generation in range(num_generations):
        evaluated_pop = evaluate_population(population)
        best_individual, best_distance = evaluated_pop[0]
        if best_distance < best_global_distance:
            best_global_distance = best_distance
            best_global_tour = best_individual[:]
        plot_tour(best_individual, generation, best_distance)
        population = new_generation(evaluated_pop, pop_size, mutation_rate)
    print("Best tour found:", best_global_tour)
    print(f"Distance: {best_global_distance:.2f}")
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()