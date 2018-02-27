import sys
import time

from Population import Population

target = 'hello world'
mutationRate = 0.01
population_size = 50
max_cycles = 500

sys.stdout.write("\nTarget: " + str(target))
sys.stdout.write("\nMutation Rate: " + str(mutationRate))
sys.stdout.write("\nPopulation Size: " + str(population_size))
sys.stdout.write("\nMax Cycles: " + str(max_cycles) + "\n\n")

start = time.time()

population = Population.create_random(population_size, len(target), target)

for i in range(max_cycles):
    population.normalize_fitness()
    best = population.get_best()
    best_string = best.to_string()
    sys.stdout.write("\rBest result: " + best_string)
    sys.stdout.flush()
    if best_string == target:
        break
    new_population = Population()
    for dna in population.pool:
        partner_a = population.get_random()
        partner_b = population.get_random()
        child = partner_a.crossover(partner_b)
        child.mutate(mutationRate)
        new_population.add(child)
    population = new_population

end = time.time()
runtime = end - start
sys.stdout.write("\nCycles needed:" + str(i + 1))
sys.stdout.write("\nTotal time:" + str(round(runtime, 2)) + "s")