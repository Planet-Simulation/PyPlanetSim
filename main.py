from functions import generate_matrix, slant, heat, ec_temp_effective
from math import cos, radians
from random import random

# Main Parameters
n_cols = 10 # Columns' number (y)
n_rows = 10 # Rows number (x)
prop_popu = 0.3 # Proportion of initial population
prop_blacks = 0.3 # Proportion of Blacks
solar_const = 1361 # Solar constant (K)
planet_alb = 0.3 # Percentage of planetary albedo

def starting_conditions(n,m,population_chance,blacks,sol_const,perc_alb):
	population = generate_matrix(n,m,0)
	colours = generate_matrix(n,m,0)
	temp_field =  generate_matrix(n,m,0)
	for i in range(0,n):
		for k in range(0,m):
			if random()<population_chance:
				population[i][k] = 1
				if random()<blacks: 
					colours[i][k] = 0.1
					temp_field[i][k] = cos(radians(slant(n,m)[i][k]))*ec_temp_effective(solar_const,0.1)
				else: 
					colours[i][k] = 0.9
					temp_field[i][k] = cos(radians(slant(n,m)[i][k]))*ec_temp_effective(solar_const,0.9)
			else:
				population[i][k] = 0
				colours[i][k] = perc_alb
				temp_field[i][k] = cos(radians(slant(n,m)[i][k]))*ec_temp_effective(solar_const,perc_alb)
	return [population,colours,temp_field]


print(starting_conditions(n_cols,n_rows,prop_popu,prop_blacks,solar_const,planet_alb))

# Salta error ya que durante las starting conditions he puestos "slant(n,m)[i][k]" pero resulta que en la función
# slant no me crea una matriz de dichas dimensiones, por lo tanto, simplemente arregla el slant, no toques nada
# de este archivo y préndelo.
