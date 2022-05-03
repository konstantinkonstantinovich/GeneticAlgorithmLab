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
        mutation_probability = request.form.get('mutation')
        crossing_over_probability = request.form.get('crossing_over')
        selection_f = request.form.get('selection_f')

        genetic_alg = GeneticAlgorithm(number_of_iterations, number_of_chromosomes, number_of_genes, mutation_probability, crossing_over_probability, selection_f)
        result = genetic_alg.epoch()
        print(result)

    return render_template('main.html', result=result)
