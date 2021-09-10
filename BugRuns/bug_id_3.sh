#!/bin/bash
cd repos/MedicalZooPytorch
source activate MLBugsMedicalZooPytorch
export PYTHONPATH=$(pwd):$PYTHONPATH

python examples/train_brats2018_new.py