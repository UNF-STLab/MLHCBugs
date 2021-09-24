#!/bin/bash
cd Repos/MedicalZooPytorch
source activate MLHCBugsMedicalZooPytorch
export PYTHONPATH=$(pwd):$PYTHONPATH

python examples/train_brats2018_new.py