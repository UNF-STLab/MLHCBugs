#!/usr/bin/env python
# MTBugs setup file. Downloads repositories with the bugs to test,
# and installs dependencies.

import os
import argparse


def make_scripts_executable():

    os.system('chmod u+x MLHCBugs_Requirements_Install.sh')
    os.system('chmod u+x MLHCBugs_Set_ID.py')

    for n in range(30):
        os.system('chmod u+x BugRuns/bug_id_' + str(n+1) + '.sh')

# Creates the repo directory if it does not exits.
def init_repos_directory():

    if not os.path.isdir('Repos'):
        os.mkdir('Repos')
        print('Repos directory initialized')

# Clones a repo at a specified commit.
def clone_repo(repo_name: str, repo_address: str, repo_commit: str):

    os.system('git clone ' + repo_address + ' Repos/' + repo_name)
    os.system('cd Repos/' + repo_name + '; git checkout ' + repo_commit)
    print('Repository ' + repo_name + 'cloned into Repos/' + repo_name +
          'HEAD at commit: ' + repo_commit)

# Removes a repo if it exists.
def remove_repo(repo_name: str):

    if os.path.isdir(repo_name):
        os.rmdir(repo_name)
        print('Repository ' + repo_name + " removed.")

# Creates a given conda env.
def create_conda_env(repo_name: str, python_v: str):

    os.system('conda create -n MLHCBugs' + repo_name + " python=" + python_v)
    print('Conda environment MLHCBugs ' + repo_name + 'created.')

# Removes a given conda env.
def remove_conda_env(env_name: str):

    os.system('conda env remove -n MLHCBugs' + env_name)
    print('Conda environment ' + env_name + ' removed.')

# Runt the dependencies install script
def install_dependencies(env_name: str, requirements_file: str):

    os.system('./MLHCBugs_Requirements_Install.sh ' +
              env_name + ' RepoRequirements/' + requirements_file)
    print(env_name + ' dependencies installed.')

# Initialize a conda env, download the repo, and intall dependencies for a repo.
def init_repo(repo_name: str, python_v: str, repo_git_address: str, repo_commit=''):

    init_repos_directory()
    remove_repo(repo_name)
    clone_repo(repo_name, repo_git_address, repo_commit)
    remove_conda_env(repo_name)
    create_conda_env(repo_name, python_v)
    install_dependencies('MLHCBugs' + repo_name, repo_name+'_requirements.txt')

# https://github.com/nyukat/breast_cancer_classifier
def init_breast_cancer_classifier():

    repository_name = 'breast_cancer_classifier'
    python_version = '3.6'
    repository_git_address = 'https://github.com/nyukat/breast_cancer_classifier.git'
    repository_commit = 'dc30252de503a87d1c4ad9ba32eacef6efca1d8d'

    init_repo(repository_name, python_version,
              repository_git_address, repository_commit)

# https://github.com/black0017/MedicalZooPytorch
def init_medical_zoo_pytorch():

    repository_name = 'MedicalZooPytorch'
    python_version = '3.6'
    repository_git_address = 'https://github.com/black0017/MedicalZooPytorch.git'
    repository_commit = '467f0c02f0468de127b814a52d3b05151e8380c6'

    init_repo(repository_name, python_version,
              repository_git_address, repository_commit)


# https: // github.com/ratschlab/RGAN
def init_RGAN():

    repository_name = 'RGAN'
    python_version = '3.5'
    repository_git_address = 'https://github.com/ratschlab/RGAN.git'
    repository_commit = '6e1ee6b484f0d26b13b952d154482cd7931eb635'

    init_repo(repository_name, python_version,
              repository_git_address, repository_commit)

# https://github.com/nilearn/nilearn
def init_nilearn():

    repository_name = 'nilearn'
    python_version = '3.6'
    repository_git_address = 'https://github.com/nilearn/nilearn.git'
    repository_commit = '2425238d4479fe1b6bee34227a4d95c252cb73e5'

    init_repo(repository_name, python_version,
              repository_git_address, repository_commit)

# https: // github.com/CamDavidsonPilon/lifelines
def init_lifelines():

    repository_name = 'lifelines'
    python_version = '3.6'
    repository_git_address = 'https://github.com/CamDavidsonPilon/lifelines.git'
    repository_commit = 'd2be007e7aea254670e244942d07df547beee603'

    init_repo(repository_name, python_version,
              repository_git_address, repository_commit)

#https://github.com/nipy/nipype
def init_nipype():

    repository_name = 'nipype'
    python_version = '3.7'
    repository_git_address = 'https://github.com/nipy/nipype.git'
    repository_commit = 'c06c03d4b65bcaa53674e671829743ffd7a2a615'

    init_repo(repository_name, python_version,
              repository_git_address, repository_commit)

#https://github.com/dipy/dipy#readme
def init_dipy():

    repository_name = 'dipy'
    python_version = '3.7'
    repository_git_address = 'https://github.com/dipy/dipy.git'
    repository_commit = 'd78e60b64a52cd140eb302d9a818d186cf560cf9'

    init_repo(repository_name, python_version,
              repository_git_address, repository_commit)

def main():

    # Arguments vector (argv)
    parser = argparse.ArgumentParser(description='Download desired repositories,' +
                                     'and their dependencies in a conda env.')

    parser.add_argument('repositories', metavar='R', type=str, nargs='+',
                        help='repositores to be tested.')

    args = parser.parse_args()

    repos = args.repositories

    make_scripts_executable()

    # Load all repos in to map and associate the init function.
    repo_dictionary = dict()

    repo_dictionary['breast_cancer_classifier'] = init_breast_cancer_classifier
    repo_dictionary['MedicalZooPytorch'] = init_medical_zoo_pytorch
    repo_dictionary['RGAN'] = init_RGAN
    repo_dictionary['nilearn'] = init_nilearn
    repo_dictionary['lifelines'] = init_lifelines
    repo_dictionary['nipype'] = init_nipype
    repo_dictionary['dipy'] = init_dipy

    # Process all args and call the function to init the desired repos.
    for repo in repos:
        repo_dictionary[repo]()


if __name__ == '__main__':

    main()
