import random

class GeneticAlgorithm:
    def __init__(self, num_iterations, num_chromosomes, num_genes, mutation, crossing_over):
        self.number_of_iterations = int(num_iterations)
        self.number_of_chromosomes = int(num_chromosomes)
        self.number_of_genes = int(num_genes)
        self.mutation_percentage = float(mutation)
        self.crossover_percentage = float(crossing_over)

    def population_initialization(self):
        return [[random.randrange(0, 2) for _ in range(self.number_of_genes) ] for _ in range(self.number_of_chromosomes)]

    def fitness(self, population):
        for individual in population:
            string_version = ''.join(map(str, individual))
            decoded = int(string_version, 2)
