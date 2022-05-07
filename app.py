from flask import Flask, render_template, request
from algorithm import GeneticAlgorithm
import time

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def main():
    result = None
    extra_result = None
    if request.method == 'POST':
        number_of_genes = request.form.get('genes')
        number_of_chromosomes = request.form.get('chromosomes')
        number_of_iterations = request.form.get('num_iterations')
        mutation_probability = request.form.get('mutation')
        crossing_over_probability = request.form.get('crossing_over')
        selection_f = request.form.get('selection_f')

        genetic_alg = GeneticAlgorithm(number_of_iterations, number_of_chromosomes, number_of_genes, mutation_probability, crossing_over_probability, selection_f)
        genetic_alg.population_initialization()
        start = time.time()
        for i in range(genetic_alg.number_of_iterations):
            genetic_alg.epoch()
            if genetic_alg.max_fitness[-1] == genetic_alg.avg_fitness[-1]:
                extra_result = f"Average and maximum converged! Avg = {genetic_alg.avg_fitness[-1]}; Max = {genetic_alg.max_fitness[-1]}"
                result = [list(range(genetic_alg.number_of_iterations)), genetic_alg.max_fitness, genetic_alg.avg_fitness]
                return render_template('result.html', result=result, extra_result=extra_result)
                break
        extra_result = f"Avg = #{genetic_alg.avg_fitness[-1]}; Max = {genetic_alg.max_fitness[-1]}"
        end = time.time()
        print(end-start)
        coordinates = genetic_alg.get_coordinates()
        result = [list(range(genetic_alg.number_of_iterations)), genetic_alg.max_fitness, genetic_alg.avg_fitness]
        return render_template('result.html', result=result, extra_result=extra_result, coordinates=coordinates)

    return render_template('main.html')
