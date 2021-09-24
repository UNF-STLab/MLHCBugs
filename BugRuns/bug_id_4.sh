#!/bin/bash
cd Repos/RGAN
source activate MLHCBugsRGAN
export PYTHONPATH=$(pwd):$PYTHONPATH

python experiment.py --settings_file test