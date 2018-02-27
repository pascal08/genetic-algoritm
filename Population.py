import random
import string

import Dna


class Population:

    def __init__(self):
        self.pool = []

    def add(self, dna: Dna):
        self.pool.append(dna)

    def get_random(self):
        pick = random.uniform(0, 1)
        total_normalized_fitness = 0.0
        for dna in self.pool:
            if total_normalized_fitness < pick < total_normalized_fitness + dna.normalized_fitness:
                return dna
            total_normalized_fitness += dna.normalized_fitness

    def normalize_fitness(self):
        total_fitness = 0
        for dna in self.pool:
            total_fitness += dna.fitness

        for dna in self.pool:
            dna.normalized_fitness = dna.fitness / total_fitness

    def get_best(self):
        highest_fitness = max(dna.fitness for dna in self.pool)
        for dna in self.pool:
            if highest_fitness == dna.fitness:
                return dna

    @staticmethod
    def create_random(size: int, target_length: int, target: string):
        random_population = Population()
        for i in range(0, size):
            random_population.add(Dna.Dna.create_random(target_length, target))
        return random_population
