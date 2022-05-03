import random
from sympy import *
from math import *

class GeneticAlgorithm:

    def __parse_fitness_func(self, func):
        return sympify(func)

    def __init__(self, num_iterations, num_chromosomes, num_genes, mutation, crossing_over, selection_f):
        self.number_of_iterations = int(num_iterations)
        self.number_of_chromosomes = int(num_chromosomes)
        self.number_of_genes = int(num_genes)
        self.mutation_probability = float(mutation)
        self.crossing_over_probability = float(crossing_over)
        self.selection_factor = float(selection_f)

    def population_initialization(self):
        return [[random.randrange(0, 2) for _ in range(self.number_of_genes) ] for _ in range(self.number_of_chromosomes)]

    def __get_bin_value(self, chromosome, position, size):
        val = 0
        for i in range(position, position+size):
            val += chromosome[i]*pow(2.0, -(i-position+1))
        return val

    def __get_fitness(self, chromosome):
        x, y = symbols('x y')
        x_value = self.__get_bin_value(chromosome, 0, len(chromosome)//2)*100.0-50.0
        y_value = self.__get_bin_value(chromosome, len(chromosome)//2, len(chromosome)//2)*100.0-50.0
        f = self.__parse_fitness_func("x**2/200 + y**2/200 + cos(x)*cos(y)")
        return -f.subs([(x, x_value), (y, y_value)])

    def selection(self, population):
        fitness_table = []
        new_population = []
        n = 0
        for chromosome in population:
            fitness_table.append(self.__get_fitness(chromosome))
        min_fitness = min(fitness_table)
        max_fitness = max(fitness_table)
        if max_fitness!=min_fitness:
            while n < self.number_of_chromosomes:
                num = random.randint(0, self.number_of_chromosomes-1)
                if self.selection_factor*random.random() < (fitness_table[num]-min_fitness)/(max_fitness-min_fitness):
                    new_population.append(population[num])
                    n+=1

        return new_population

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
                    pos = random.randint(1, self.number_of_genes)
                    for k in range(pos):
                        temp = population[i][k]
                        population[i][k] = population[j][k]
                        population[j][k] = temp
        return population

    def epoch(self):
        for _ in range(self.number_of_iterations):
            population = self.population_initialization()
            mutation = self.mutation(population)
            crossing_over = self.crossing_over(mutation)
            result = self.selection(crossing_over)
            print(result)
