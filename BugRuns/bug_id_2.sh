#!/bin/bash
cd Repos/MedicalZooPytorch
source activate MLHCBugsMedicalZooPytorch
export PYTHONPATH=$(pwd):$PYTHONPATH

python tests/test_miccai_2019.py --dataset_name MICCAI_2019_pathology_challenge --nEpochs 2 --opt adam --model UNET2D