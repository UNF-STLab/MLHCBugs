#!/usr/bin/env python
#MLHC Bugs testing file.

import os
import argparse

def get_commit_id(repo_name:str):

    commit_id_file = open('Repos/' + repo_name + '/.git/head', 'r')
    commit_id = commit_id_file.read()

def bug_test_breast_cancer_classifier(bug_id:int):

    commit_id = get_commit_id('breast_cancer_classifier')

    if bug_id == 1:

        if commit_id != 'dc30252de503a87d1c4ad9ba32eacef6efca1d8d':
           os.system('cd Repos/breast_cancer_classifier; git checkout ' +
                        'dc30252de503a87d1c4ad9ba32eacef6efca1d8d')

        os.system('./BugRuns/bug_id_1.sh')

def bug_test_medical_zoo_pytorch(bug_id:int):

    commit_id = get_commit_id('MedicalZooPytorch')

    if bug_id == 2:

        if commit_id != '467f0c02f0468de127b814a52d3b05151e8380c6':
           os.system('cd Repos/MedicalZooPytorch; git checkout ' +
                        '467f0c02f0468de127b814a52d3b05151e8380c6')
        
        os.system('./BugRuns/bug_id_2.sh')

    if bug_id == 3:

        if commit_id != '4a90346c3d6e445712089c6bf13cbae00b43c35b':
           os.system('cd Repos/MedicalZooPytorch; git checkout ' + 
                        '4a90346c3d6e445712089c6bf13cbae00b43c35b')

        os.system('./BugRuns/bug_id_3.sh')

def bug_test_RGAN(bug_id: int):

    commit_id = get_commit_id('RGAN')

    if bug_id == 4:

        if commit_id != '6e1ee6b484f0d26b13b952d154482cd7931eb635':
           os.system('cd Repos/RGAN; git checkout ' +
                     '6e1ee6b484f0d26b13b952d154482cd7931eb635')

        os.system('./Tests/bug_id_4.sh')

def main():

    # Arguments vector (argv)
    parser = argparse.ArgumentParser(description='Test bugs based on ID')

    parser.add_argument('bug_ids', metavar='B', type=int, nargs='+',
                        help='Bugs to be tested.')

    args = parser.parse_args()

    bug_ids = args.bug_ids

    # Load all repos in to map and associate the init function.
    bug_dictionary = dict()

    bug_dictionary[1] = bug_test_breast_cancer_classifier
    bug_dictionary[2] = bug_test_medical_zoo_pytorch
    bug_dictionary[3] = bug_test_medical_zoo_pytorch
    bug_dictionary[4] = bug_test_RGAN

    bugs = bug_dictionary.keys()

    # Process all args and call the function to init the desired repos.
    for bug_id in bug_ids:
        bug_dictionary[bug_id](bug_id)
    
if __name__ == '__main__':

    main()
