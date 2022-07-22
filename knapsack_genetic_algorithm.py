import random
import numpy as np


def fitness(individual):         # fitness function that return our total profit if its valid

    total_weight = 0
    total_price = 0
    for i in range(n):
        total_weight += individual[i] * W_item[i]
        total_price += individual[i] * P_item[i]
    if total_weight > W:         # if total_weight is bigger than W then return 0
        return 0
    else:
        return total_price


def Genetic_Algotithm(population, fitness_func, n_generations):  # main genetic algorithm

    for i in range(n_generations):                        # do for n generations   
        new_population = list()                           # initialize new_population as an empty list
        if not acceptable(population, fitness_func):      # if our population is not acceptable (all the profits are 0) then continue to next generation
            continue
        for j in range(len(population)):                  
            x = random_selection(population, fitness_func)  # select a parent randomly(higher score higher chance)
            y = random_selection(population, fitness_func)  # select a parent randomly(higher score higher chance)
            child = reproduce(x[0], y[0])           # reproduce our child
            if random.random() <= 0.2:              # mutate if a small probability
                child = mutation(child)
            new_population.append(child)
        if average_population_score(new_population, fitness_func) > average_population_score(population, fitness_func):
            population =  new_population         # if averege score of new population is bigger that previous population then update population

    return best_individual(population, fitness_func)      # at the end return the best individual in the population


def random_selection(population, fitness_func):       
    scores = list()          # a list that contains scores of the individuals
    percent = list()         # a list that contains percent of each individual based on their fitness score
    for individual in population:
        scores.append(fitness_func(individual))      # add fitness score to scores list
    for score in scores:
        percent.append(round((score / sum([x for x in scores])) * 100))   # add percent to percent list
    return random.choices(population, weights=percent, k=1)               # choose a individual from population based on their weight (percent)


def reproduce(x, y):      # reproduce a child from two parents

    n = len(x)
    c = random.randint(1, n)    # choose a random crossover
    child = x[:c] + y[c:]
    return child


def mutation(individual):  # mutate an individual

    index = random.randint(0, len(individual)-1)
    individual[index] = 1 if individual[index] == 0 else 0      # change a random bit
    return individual


def best_individual(population, fitness_func):       # return best individual in the population based on their score
    lst = list()
    for individual in population:
        lst.append(fitness_func(individual))
    return population[lst.index(max(lst))]


def average_population_score(population, fitness_func):   # return average score in the population
    lst = list()
    for individual in population:
        lst.append(fitness_func(individual))
    return sum(lst) / len(lst)


def acceptable(population, fitness_func):      # return false if score of all the individual is 0 else return true
    for individual in population:
        if fitness_func(individual) > 0:
            return True
    return False


W = 190                        
n = 6                          
W_item = [56, 59, 80, 64, 75, 17]          
P_item = [50, 50, 64, 46, 50, 5]           


initial_population = np.random.randint(2, size = (10, n))    # initialize population randomly
initial_population = initial_population.astype(int)
initial_population = initial_population.tolist()

max_profit = 0

for i in range(10):                # repeat algorithm 10 times to get the best result
    solution =  Genetic_Algotithm(initial_population, fitness, 600)
    if fitness(solution) > max_profit:
        max_profit = fitness(solution)
        best_solution = solution

print("solution: ", solution)
print("max_profit: ", max_profit)
