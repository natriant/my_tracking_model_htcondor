# read the parameters from the oconfig.json file
# Cretate 1 directory for each study
# cretate the my_tracking.py for each study from the template

import os
import json
import numpy as np

data = {}

with open('./config.json', "r") as read_file:
	data = json.load(read_file)


# iteration over different parameters, iteration over different values of the working point should be added/
if data['BB']['status']:
	BB_list = np.geomspace(data['BB']['values_limits']['min'], data['BB']['values_limits']['max'], data['BB']['values_limits']['step']) # this should be chamged to logarithmic scale
else:
	BB_list = [0.0]


if data['Noise']['status']:
        Noise_list = np.geomspace(data['Noise']['values_limits']['min'], data['Noise']['values_limits']['max'], data['Noise']['values_limits']['step']) # this should be chamged to logarithmic scale
else:
        Noise_list = [0.0]


if data['Feedback']['status']:
        Feedback_list = np.geomspace(data['Feedback']['values_limits']['min'], data['Feedback']['values_limits']['max'], data['Feedback']['values_limits']['step']) # this should be chamged to logarithmic scale
else:
        Feedback_list = [0.0]


#create the list with the names of the studies and a directory for each study, open my_tracking_template.py and replace the parameters
my_studies_list = []
for xi in BB_list:
	for delta in Noise_list:
		for g in Feedback_list:
                        # Create the name of the study, according to the elements that are present, maybe create a seperate function afterwards		  
			name = 'Qx{:.3f}_Qy{:.3f}_xi{:.3f}_g{:.3f}_delta{:.3f}_betax{}_betay{}_particles{}_turns{}'.format(data['machine_parameters']['Qx_init'], data['machine_parameters']['Qy_init'], xi, g, delta, data['machine_parameters']['beta_x'], data['machine_parameters']['beta_y'], data['study_parameters']['particles'],  data['study_parameters']['turns'])
			
			if data['octupole']['status']: #introduce tune spread with octupole instead of BB
				name = 'Qx{:.3f}_Qy{:.3f}_k3_int{:.3f}_segments{}_g{:.3f}_delta{:.3f}_betax{}_betay{}_particles{}_turns{}'.format(data['machine_parameters']['Qx_init'], data['machine_parameters']['Qy_init'], data['octupole']['k3_int'] , data['study_parameters']['segments'], g, delta, data['machine_parameters']['beta_x'], data['machine_parameters']['beta_y'], data['study_parameters']['particles'],  data['study_parameters']['turns'])
			if data['Amplitude_Detuner']['status']: # introduce tune spread with amplitude, with phase advance (like the one from an octupole)
				name = 'Qx{:.3f}_Qy{:.3f}_detunerx{:.3f}_detunery{:.3f}_g{:.3f}_delta{:.3f}_betax{}_betay{}_particles{}_turns{}'.format(data['machine_parameters']['Qx_init'], data['machine_parameters']['Qy_init'], data['Amplitude_Detuner']['k3_equivalent_x'], data['Amplitude_Detuner']['k3_equivalent_y'], g, delta, data['machine_parameters']['beta_x'], data['machine_parameters']['beta_y'],  data['study_parameters']['particles'],  data['study_parameters']['turns'])

			my_studies_list.append(name)
			# create the direcotry for the study
			if not os.path.exists(name):
				os.makedirs(name)
				os.makedirs(name + '/error')
				os.makedirs(name+'/output')
				os.makedirs(name+'/log')

			# Open the template file here
			f= open('./my_tracking_template', 'r')
			linelist = f.readlines()
			f.close
			
			# old words
			checkWords = ('%f_rev', '%gamma_rel', '%betax', '%betay', '%alphax', '%alphay', '%Qx_init', '%Qy_init', '%turns', '%particles', '%ex_norm', '%ey_norm', '%flag_oct', '%flag_noise', '%flag_BB', '%flag_feedback', '%flag_detuner', '%max_aperture_value', '%k3_int', '%k3_equivalent_x', '%k3_equivalent_y', '%segments', '%delta', '%ksi', '%g')
			
			g_str = "{}".format(g)
			xi_str = "{}".format(xi)	

			# new words
			repWords = (str(data['machine_parameters']['f_rev']), str(data['machine_parameters']['gamma_rel']), str(data['machine_parameters']['beta_x']), str(data['machine_parameters']['beta_y']), str(data['machine_parameters']['alpha_x']) , str(data['machine_parameters']['alpha_y']), str(data['machine_parameters']['Qx_init']), str(data['machine_parameters']['Qy_init']), str(data['study_parameters']['turns']),  str(data['study_parameters']['particles']), str(data['study_parameters']['ex_norm']), str(data['study_parameters']['ex_norm']), str(data['octupole']['status']), str(data['Noise']['status']), str(data['BB']['status']), str(data['Feedback']['status']), str(data['Amplitude_Detuner']['status']),str(data['study_parameters']['aperture_max']), str(data['octupole']['k3_int']), str(data['Amplitude_Detuner']['k3_equivalent_x']), str(data['Amplitude_Detuner']['k3_equivalent_y']), str(data['study_parameters']['segments']), str(delta), xi_str,g_str)


			# Open the new file here
			f2 = open(name+'/my_tracking.py', 'w')
			for line in linelist:
    				for check, rep in zip(checkWords, repWords):
        				line = line.replace(check, rep)
    				f2.write(line)
			f2.close()




print(my_studies_list)		 



# open the my_tracking_template.py and replace the parameters. Then copy it 
