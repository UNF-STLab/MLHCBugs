#!/bin/bash
cd repos/RGAN
source activate MLBugsRGAN
export PYTHONPATH=$(pwd):$PYTHONPATH

python experiment.py --settings_file test