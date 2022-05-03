import random
from sympy import *

class GeneticAlgorithm:

    def __parse_fitness_func(self, fitness):
        return sympify(fitness)

    def __init__(self, num_iterations, num_chromosomes, num_genes, mutation, crossing_over, fitness_func):
        self.number_of_iterations = int(num_iterations)
        self.number_of_chromosomes = int(num_chromosomes)
        self.number_of_genes = int(num_genes)
        self.mutation_probability = float(mutation)
        self.crossing_over_probability = float(crossing_over)
        self.fintess_function = self.__parse_fitness_func(fitness_func)

    def population_initialization(self):
        return [[random.randrange(0, 2) for _ in range(self.number_of_genes) ] for _ in range(self.number_of_chromosomes)]

    def get_fitness(self):
        self.fintess_function.free_symbols
        x, y = symbols('x y')
        return self.fintess_function.free_symbols

    def mutation(self, population):
        for chromosome in range(self.number_of_chromosomes):
            for gene in range(self.number_of_genes):
                if random.random() < self.mutation_probability:
                    population[chromosome][gene] = 1 - population[chromosome][gene]
        return population

    def crossing_over(self, population):
        for i in range(self.number_of_chromosomes):
            if random.random() < self.crossing_over_probability:
                j = random.randint(0, self.number_of_chromosomes-1)
                if (i!=j):
                    pos = random.randint(1, self.number_of_genes-1)
                    for k in range(pos):
                        temp = population[i][k]
                        population[i][k] = population[j][k]
                        population[j][k] = temp
        return population

    # def get_fitness(self, individual):
        # for individual in population:
        #     string_version = ''.join(map(str, individual))
        #     decoded = int(string_version, 2)
