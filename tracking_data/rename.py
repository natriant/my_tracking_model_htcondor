# Each simulation in ../my_tracking_model_htcondor should be repeated three times and the emittance growth avergaed over rans is estiamted.
# Therefore we neeed to rename the pickle files produced by the tracking scripts.
# How it works:
# 1. part A: Given that this script runs exactly after the pickle files that are stored in this directory the .json file is open so you can access the details of thestudy.
# 2. part B: Give the number of the current version 
# 3. part C: Find the files in the directory and add the suffix that corresponds to the version.


 
import os
import json
import numpy as np

# A. Open config.json file to access the parameters of the study
data = {}

with open('../config.json', "r") as read_file:
        data = json.load(read_file)

# variable to iterate 
Delta_list = np.geomspace(data['Noise']['values_limits']['min'], data['Noise']['values_limits']['max'], data['Noise']['values_limits']['step']) # this should be chamged to logarithmic scale

#B. Give the number of the current version
version = 3

#C. Find the files in the directory and add the suffix that corresponds to the version. 


for Delta in Delta_list:
	for filename in os.listdir():
		current_name = 'Qx62.775_k3_int5825.61_g0.200_delta{:.3f}_betax115.75_particles15000_turns1000.pkl'.format(Delta) 
		if current_name == filename:
			os.replace(current_name, 'Qx62.775_k3_int5825.61_g0.200_delta{:.3f}_betax115.75_particles15000_turns1000_v{}.pkl'.format(Delta, version))
