import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np
from math import *

df = pd.read_pickle('Qx62.775_k3_int5825.61_g0.200_delta1.000_betax115.75_particles15000_turns1000.pkl')
#print(df.at[800,'px'])

# Set True the corresponding flag
plot_evolution_of_a_particle = False
plot_evolution_of_the_mean = False
print_info_for_each_aprticle = True


if print_info_for_each_aprticle:
	for particle in range(15000):
		for turn in range(1000):
			#print(df.at[turn,'px'][1])
			if isnan(df.at[turn,'px'][particle]):
				print('the first NaN for particle {} found at turn {}:'.format(particle, turn))
				#print('for particle {},  last three px values are {}, {}, {}'.format(particle, df.at[turn-2, 'px'][particle],  df.at[turn-1, 'px'][particle],  df.at[turn, 'px'][particle]))
				break


if plot_evolution_of_a_particle:
	particle_number = 157
	for turn in range(1000):
		plt.plot(turn, df.at[turn,'px'][particle_number], '.')
	plt.show()


if plot_evolution_of_the_mean:
	for turn in range(1000):
		plt.plot(turn, np.mean(df.at[turn,'x']), '.')
