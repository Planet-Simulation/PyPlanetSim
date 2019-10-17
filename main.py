from functions import generate_matrix, slant, heat
from math import cos, radians
from random import random


def starting_conditions(n,m,population_chance,blacks):
	population = generate_matrix(n,m,0)
	colours = generate_matrix(n,m,0)
	for i in range(0,n):
		for k in range(0,m):
			if random()<population_chance:
				population[i][k] = 1
				if random()<blacks: colours[i][k] = 1
				else: colours[i][k] = 0
			else:
				population[i][k] = 0
				colours[i][k] = -1
	return [population,colours]



#while (final_conditions==False):

