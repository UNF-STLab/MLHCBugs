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

        os.system('./BugRuns/bug_id_4.sh')
    
def bug_test_nilearn(bug_id: int):

    commit_id = get_commit_id('nilearn')

    if bug_id == 5:

        if commit_id != '2425238d4479fe1b6bee34227a4d95c252cb73e5':
           os.system('cd Repos/nilearn; git checkout ' +
                     '2425238d4479fe1b6bee34227a4d95c252cb73e5')

        os.system('./BugRuns/bug_id_5.sh')

    if bug_id == 6:

        if commit_id != '89b4e799a229ca4b1a11a12d9e486fa0cc3ab274':
           os.system('cd Repos/nilearn; git checkout ' +
                     '89b4e799a229ca4b1a11a12d9e486fa0cc3ab274')

        os.system('./BugRuns/bug_id_6.sh')

    if bug_id == 7:

        if commit_id != 'ac1a934e3b2b4061f894b518c960412df9ea4f11':
           os.system('cd Repos/nilearn; git checkout ' +
                     'ac1a934e3b2b4061f894b518c960412df9ea4f11')

        os.system('./BugRuns/bug_id_7.sh')

    if bug_id == 8:

        if commit_id != 'f47d6f58577d2b3bec51c3eba2e35dac3ad625c6':
           os.system('cd Repos/nilearn; git checkout ' +
                     'f47d6f58577d2b3bec51c3eba2e35dac3ad625c6')

        os.system('./BugRuns/bug_id_8.sh')

    if bug_id == 9:

        if commit_id != '01647c2c0d69a227124d8834a0bbb46a6acf0927':
           os.system('cd Repos/nilearn; git checkout ' +
                     '01647c2c0d69a227124d8834a0bbb46a6acf0927')

        os.system('./BugRuns/bug_id_9.sh')

    if bug_id == 10:

        if commit_id != 'd32890c2477d82848aee953156b27e14559b21eb':
           os.system('cd Repos/nilearn; git checkout ' +
                     'd32890c2477d82848aee953156b27e14559b21eb')

        os.system('./BugRuns/bug_id_10.sh')

    if bug_id == 11:

        if commit_id != '1f14723938e892801a9736481b588982d298ba48':
           os.system('cd Repos/nilearn; git checkout ' +
                     '1f14723938e892801a9736481b588982d298ba48')

        os.system('./BugRuns/bug_id_11.sh')

    if bug_id == 12:

        if commit_id != '0c2c84aabb69ca73f2d78c3488b7afc2bc130ab3':
           os.system('cd Repos/nilearn; git checkout ' +
                     '0c2c84aabb69ca73f2d78c3488b7afc2bc130ab3')

        os.system('./BugRuns/bug_id_12.sh')

    if bug_id == 13:

        if commit_id != '398ab45ba1a611ace5c603f04ee4fa8ef1ff115c':
           os.system('cd Repos/nilearn; git checkout ' +
                     '398ab45ba1a611ace5c603f04ee4fa8ef1ff115c')

        os.system('./BugRuns/bug_id_13.sh')

    if bug_id == 14:

        if commit_id != '8e972c4d382a74fb126f768a0ae02e01e817515c':
           os.system('cd Repos/nilearn; git checkout ' +
                     '8e972c4d382a74fb126f768a0ae02e01e817515c')

        os.system('./BugRuns/bug_id_14.sh')
    
    if bug_id == 15:

        if commit_id != '99d878d6d78c3f5250bc0d627b651c66d9b9ec9f':
           os.system('cd Repos/nilearn; git checkout ' +
                     '99d878d6d78c3f5250bc0d627b651c66d9b9ec9f')

        os.system('./BugRuns/bug_id_15.sh')

def bug_test_lifelines(bug_id: int):

    commit_id = get_commit_id('lifelines')

    if bug_id == 16:

        if commit_id != 'd2be007e7aea254670e244942d07df547beee603':
           os.system('cd Repos/lifelines; git checkout ' +
                     'd2be007e7aea254670e244942d07df547beee603')

    if bug_id == 17:

        if commit_id != 'cb22e7ffcfbcadf59c8bc3094206a1a2a46fd6cf':
           os.system('cd Repos/lifelines; git checkout ' +
                     'cb22e7ffcfbcadf59c8bc3094206a1a2a46fd6cf')
    
    if bug_id == 18:

        if commit_id != '2a23205548e8c69115f145ca195899418dd380ee':
           os.system('cd Repos/lifelines; git checkout ' +
                     '2a23205548e8c69115f145ca195899418dd380ee')

    if bug_id == 19:

        if commit_id != '8f64de9d16425b232532977de43519bfbfdbb34a':
           os.system('cd Repos/lifelines; git checkout ' +
                     '8f64de9d16425b232532977de43519bfbfdbb34a')
    
    if bug_id == 20:

        if commit_id != '3fe06bc23b53383721dd6efdd54b7ec9a454137d':
           os.system('cd Repos/lifelines; git checkout ' +
                     '3fe06bc23b53383721dd6efdd54b7ec9a454137d')

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
    bug_dictionary[5] = bug_test_nilearn
    bug_dictionary[6] = bug_test_nilearn
    bug_dictionary[7] = bug_test_nilearn
    bug_dictionary[8] = bug_test_nilearn
    bug_dictionary[9] = bug_test_nilearn
    bug_dictionary[10] = bug_test_nilearn
    bug_dictionary[11] = bug_test_nilearn
    bug_dictionary[12] = bug_test_nilearn
    bug_dictionary[13] = bug_test_nilearn
    bug_dictionary[14] = bug_test_nilearn
    bug_dictionary[15] = bug_test_nilearn
    bug_dictionary[16] = bug_test_lifelines
    bug_dictionary[17] = bug_test_lifelines
    bug_dictionary[18] = bug_test_lifelines
    bug_dictionary[19] = bug_test_lifelines
    bug_dictionary[20] = bug_test_lifelines


    bugs = bug_dictionary.keys()

    # Process all args and call the function to init the desired repos.
    for bug_id in bug_ids:
        bug_dictionary[bug_id](bug_id)
    
if __name__ == '__main__':

    main()
