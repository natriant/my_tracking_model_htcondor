#!/bin/bash
echo "uname -r:" `uname -r`

DIR=/afs/cern.ch/work/n/natriant/private/my_tracking_model_htcondor

export MYPYTHON=~/miniconda2

source $MYPYTHON/bin/activate ""
export PATH=$MYPYTHON/bin:$PATH

echo "which python:" `which python`


#python /afs/cern.ch/work/n/natriant/private/linear_map_htcondor/test5/script.py
python $DIR/%index1/my_tracking.py

