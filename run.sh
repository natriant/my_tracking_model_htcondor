#!/bin/bash

DIR=/afs/cern.ch/work/n/natriant/private/my_tracking_model_htcondor


for i in *Qx*
do
	
	cd $DIR/$i
        cp $DIR/submission_file.sub ./


	sed -e 's/%index1/'$i'/g' $DIR/my_executable_template.sh > $DIR/$i/my_executable.sh
	chmod +x my_executable.sh
	condor_submit submission_file.sub
        cd ..
done
