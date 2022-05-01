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
        crossover_percentage = request.form.get('crossing_over')

        genetic_alg = GeneticAlgorithm(number_of_iterations, number_of_chromosomes, number_of_genes, mutation_percentage, crossover_percentage)
        population = genetic_alg.population_initialization()
        genetic_alg.fitness(population)

    return render_template('main.html', result=result)
