import random
import string


class Dna:
    def __init__(self, genes: list, target: string):
        self.genes = genes
        self.target = target
        self.fitness = 0
        self.normalized_fitness = 0
        self.calc_fitness()

    def calc_fitness(self):
        score = 0
        for index, gene in enumerate(self.genes):
            if gene == self.target[index]:
                score += 1
        self.fitness = max(1, pow(score, 5))

    def crossover(self, partner: 'Dna') -> 'Dna':
        own_genes = self.genes[:len(self.genes)//2]
        partner_genes = partner.genes[len(partner.genes)//2:]
        return Dna(own_genes + partner_genes, self.target)

    @staticmethod
    def create_random(size: int, target: string) -> 'Dna':
        return Dna([(random.choice(list('abcdefghijnklmnopqrstuvwxyz '))) for i in range(size)], target)

    def to_string(self):
        return ''.join(self.genes)

    def mutate(self, chance: float):
        for index in range(len(self.genes)):
            if random.uniform(0, 1) < chance:
                self.genes[index] = random.choice(list('abcdefghijnklmnopqrstuvwxyz '))
