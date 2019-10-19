from math import cos, radians

generate_matrix = lambda y,x,a: [[a for x in range(x)] for i in range(y)]
ec_temp_effective = lambda K,a: ((K*(1-a))/(4*5.6705*10**(-8)))**(1/4) # Temperatura effective's ecuation

def slant(n,m):
	inclination = []
	angle = 180/(n-1)
	inclination.append(generate_matrix(1,m,0))
	for apex in range(1,int((n-1)/2)): # For each different latitude, the same angle is added to de matrix in the 0-position and in the last position.
		c_angle = angle*apex
		row_n = []
		for i in range(0,m): row_n.append(c_angle)
		inclination.append(row_n)
		inclination.insert(0,row_n)
	return inclination

def heat(inclination,temperature_field,colours,K):
	new_temperature_field = generate_matrix(len(inclination),len(inclination[0]), 0)
	for i in range(0,len(inclination)):
		for k in range(0,len(inclination[0])):
			sun_heat = (cos(radians(inclination[i][k]))*ec_temp_effective(K,colours[i][k]))
			neigh_warm = (temperature_field[i+1][k]+temperature_field[i-1][k]+temperature_field[i][k+1]+temperature_field[i][k-1])/4
			new_temperature_field[i][k] = 0.4*(sun_heat+temperature_field[i][k])+neigh_warm*0.2
	return new_temperature_field

