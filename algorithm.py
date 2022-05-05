import random
from sympy import *
from math import *

class GeneticAlgorithm:

    def __init__(self, num_iterations, num_chromosomes, num_genes, mutation, crossing_over, selection_f):
        self.number_of_iterations = int(num_iterations)
        self.number_of_chromosomes = int(num_chromosomes)
        self.number_of_genes = int(num_genes)
        self.mutation_probability = float(mutation)
        self.crossing_over_probability = float(crossing_over)
        self.selection_factor = float(selection_f)
        self.max_fitness = []
        self.avg_fitness = []
        self.population = []
        self.fitness_table = []


    def population_initialization(self):
        self.population = [[random.randint(0, 1) for _ in range(self.number_of_genes) ] for _ in range(self.number_of_chromosomes)]

    def __get_bin_value(self, chromosome, position, size):
        val = 0
        for i in range(position, position+size):
            val += chromosome[i]*pow(2.0, -(i-position+1))
        return val

    def __get_fitness(self, chromosome):
        x, y = symbols('x y')
        x_value = self.__get_bin_value(chromosome, 0, self.number_of_genes)*100.0-50.0
        # y_value = self.__get_bin_value(chromosome, self.number_of_genes//2, self.number_of_genes//2)*100.0-50.0
        f = simplify("x**2 + 4", transformations='all')
        result = f.subs([(x, x_value)])
        self.fitness_table.append(result)
        return result

    def selection(self):
        new_population = []
        n = 0
        self.population.sort(key=self.__get_fitness, reverse=True)
        min_fitness = self.fitness_table[-1]
        max_fitness = self.fitness_table[0]
        self.max_fitness.append(max_fitness)
        self.avg_fitness.append(sum(self.fitness_table)/self.number_of_chromosomes)
        if max_fitness!=min_fitness:
            while n < self.number_of_chromosomes:
                num = random.randint(0, self.number_of_chromosomes-1)
                if (self.selection_factor*random.random()) < ((self.fitness_table[num]-min_fitness)/(max_fitness-min_fitness)):
                    new_population.append(self.population[num])
                    n+=1
            self.population = new_population
        self.fitness_table = []

    def mutation(self):
        for i in range(self.number_of_chromosomes):
            for j in range(self.number_of_genes):
                if random.random() < self.mutation_probability:
                    self.population[i][j] = 1 - self.population[i][j]

    def crossing_over(self):
        for i in range(1, self.number_of_chromosomes, 2):
            if random.random() < self.crossing_over_probability:
                pos = random.randint(1,self.number_of_genes-1)
                first_gene = self.population[i-1]
                second_gene = self.population[i]
                self.population[i-1] = first_gene[:pos] + second_gene[pos:]
                self.population[i] = second_gene[:pos] + first_gene[pos:]

    def epoch(self):
        self.mutation()
        self.crossing_over()
        self.selection()
