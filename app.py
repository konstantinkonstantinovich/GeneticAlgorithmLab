from flask import Flask, render_template, request
from algorithm import GeneticAlgorithm

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def main():
    result = None
    if request.method == 'POST':
        number_of_genes = request.form.get('genes')
        number_of_chromosomes = request.form.get('chromosomes')
        number_of_iterations = request.form.get('num_iterations')
        mutation_percentage = request.form.get('mutation')
        crossing_over_percentage = request.form.get('crossing_over')
        fitness_function = request.form.get('fitness_func')

        genetic_alg = GeneticAlgorithm(number_of_iterations, number_of_chromosomes, number_of_genes, mutation_percentage, crossing_over_percentage, fitness_function)
        population = genetic_alg.population_initialization()
        # genetic_alg.fitness(population)
        print(population)
        mutation = genetic_alg.mutation(population)
        print(mutation)
        crossing_over = genetic_alg.crossing_over(mutation)
        print(crossing_over)

    return render_template('main.html', result=result)
