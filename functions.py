from math import cos, radians

def generate_matrix(y,x,a):
	matrix = []
	for i in range(0,y):
		row = []
		for k in range(0,x):
			row.append(a)
		matrix.append(row)
	return matrix

def slant(n,m):
	inclination = []
	angle = 180/(n-1)
	inclination.append(generate_matrix(1,m,0)[0])
	for apex in range(1,int((n-1)/2)): #for each different latitude, the same angle is added to de matrix in the 0-position and in the last position.
		c_angle = angle*apex
		row_n = []
		for i in range(0,m): row_n.append(c_angle)
		inclination.append(row_n)
		inclination.insert(0,row_n)

	return inclination


def heat(inclination,temperature_field,sun_h):
	new_temperature_field = generate_matrix(len(inclination),len(inclination[0]))
	for i in range(0,len(inclination)):
		for k in range(0,len(inclination[0])):
			sun_heat = cos(radians(inclination[i][k]))*sun_h
			new_temperature_field[i][k] = (sun_heat+temperature_field[i][k])/2

	return new_temperature_field

