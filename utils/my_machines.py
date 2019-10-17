from dotted_dict import DottedDict
from my_elements import *
import numpy as np

def my_machine(Qx_init, Qy_init, segments, k3, turn, bunch, twiss, flag_oct, flag_noise, flag_BB, flag_feedback, Delta = 0., ksi = 0., gain = 0., sigmax = 0., sigmapx = 0., sigmay=0., sigmapy = 0.):
	if turn == 1:
        	print('flag_oct {}, flag_noise {}, flag_BB {}, flag_feedback {}'.format(flag_oct, flag_noise, flag_BB, flag_feedback))
	for segment in range(segments):
		bunch.x, bunch.px, bunch.y, bunch.py = rotation(Qx_rot = Qx_init/segments, Qy_rot = Qy_init/segments, twiss = twiss, x = bunch.x, px = bunch.px, y = bunch.y, py=bunch.py)
	if flag_oct:
		bunch.x, bunch.px, bunch.y, bunch.py = octupole_map(k3/segments, x = bunch.x, px = bunch.px, y = bunch.y, py=bunch.py)
	if flag_noise and (segment == segments-1):
		if turn ==1 :
			print('Delta',Delta)
		bunch.x, bunch.px, bunch.y, bunch.py = noise_map(Delta, x = bunch.x, px = bunch.px, y = bunch.y, py=bunch.py)
	if flag_BB and (segment == segments-1):
		if turn ==1:
			print('ksi{}, sigmax{}, sigmapx{}, sigmay{}, sigmapy{}'.format(ksi, sigmax, sigmapx, sigmay, sigmapy))
		bunch.x, bunch.px, bunch.y, bunch.py = BB_4D_map(ksi, sigmax, sigmapx, sigmay, sigmapy, x= bunch.x, px = bunch.px, y = bunch.y, py=bunch.py)
        

	# Introduce aperture limitations, if the amplitude of the particles > 1m they are considered lost
	# if ampltiude > 1m make it NaN. When the average is calculated for the feedback kick, the NaN values are ignored (numpy.nanmean)
	
	my_coordiante_arrays = [bunch.x, bunch.px, bunch.y, bunch.py]
	for my_coordinate_array in my_coordiante_arrays:
		for index in range(len(my_coordinate_array)):
			if my_coordinate_array[index] > 1.:
				my_coordinate_array[index]=np.nan   	

	if flag_feedback and (segment == segments-1):
		if turn ==1:
			print('g',gain)
		bunch.x, bunch.px, bunch.y, bunch.py = feedback_system_map(gain, sigmapx, x= bunch.x, px = bunch.px, y = bunch.y, py=bunch.py)
	
	return bunch
