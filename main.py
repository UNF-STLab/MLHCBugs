#!/usr/bin/env python
# coding: utf-8

# A Python Framework that automatically prepares Conda environments and runs saved/given
# Python scripts to reproduce bugs in packages and repositories. The process of preparing
# the Conda environment includes installing the specific version of the package under test
# and its dependencies from Conda, PyPI and GitHub repositories.
# 
# Author: Nazmul Kazi

# # Import Packages

from typing import Union, List
import argparse, json, os, re, shutil, subprocess as sp, yaml


# # Methods
# ## Helper Methods

def clone_repo(name: str, url: str, commit_id: str) -> None:
    """
    Clones a remote Git repository and checks out a specific commit.

    Arguments:
        name (str): The name of the repository. This name will be used to create the local directory inside which the repository will be cloned.
        url (str): The URL of the remote Git repository to clone.
        commit_id (str): The ID of the commit to check out after cloning.
    """

    # Download the repository. If the repository already exists locally,
    # Git will not download the repository again and ignore the command.
    print('Downloading repo...'.ljust(35), end='', flush=True)
    command = f'git clone {url} repos/{name}'
    out = sp.run(command, shell=True, capture_output=True, text=True)
    print('[Done]', flush=True)
    
    # Checkout the commit of the given id.
    # WARNING: All local changes and untracked files/directories inside the repository will be thrown away.
    print('Preparing repo...'.ljust(35), end='', flush=True)
    command = f'git checkout --force {commit_id}'
    sp.run(command, cwd=f'repos/{name}/', shell=True, capture_output=True, text=True)
    print('[Done]', flush=True)


def run_command(command: Union[str, List[str]], *, env: str = None, **other_run_kwargs) -> sp.CompletedProcess:
    """
    Runs command in the environment of the current process or a conda environment.
    
    Arguments:
        command (Union[str, List[str]]): The command to execute.
        env (str, optional): The path to the conda environment to use.
    """
    
    # If no conda environment path (env_path) is given, `env` is set to None to execute the
    # given command in the environment of the current process. Otherwise, `env` is set to
    # a mapping of updates environment variables to run the given command using the conda
    # environment located at the given path. `CONDA_PREFIX` environment variable designates
    # the root directory of the currently active conda environment. Thus, `CONDA_PREFIX` is
    # set to the given environment path. The environment variable `PATH` is prefixed with
    # the location of the `bin` directory inside the given conda environment to ensure that
    # the subprocess uses the Python interpreter and binaries of the given conda environment.
    return sp.run(command, env={'CONDA_PREFIX': env, 'PATH': os.pathsep.join([os.path.join(env, 'bin'), os.environ['PATH']])} if env else None, **other_run_kwargs)


def prepare_conda_env(env_path: str, repo: str, version: str, install_repo_only: bool = False) -> bool:
    """
    Prepares a conda environment and/or installs the repository as a dependency in the created or existing environment.

    Arguments:
        env_path (str): The path where the conda environment will be created.
        repo (str): The name of the repository or Python package under test.
        version (str): The version of the Python package (must follow the version scheme outlined in PEP 440) or the commit id (full hash) of the repository.
        install_repo_only (bool, optional): If True, only installs the repository on the existing conda environment. Defaults to False.

    Returns:
        bool: True if all operations are successful; otherwise, False or None.
    """

    # Method to print process stdout and stderr into a single string along with horizontal separators
    def print_output(cp: sp.CompletedProcess) -> None:
        hline = '-' * 36; print('[Failed]', f'{hline} STDOUT {hline}', cp.stdout, f'{hline} STDERR {hline}', cp.stderr, f'{hline} STDEND {hline}', sep='\n', flush=True)

    # The version is either a Python package version or a hash. According to PEP 440,
    # a valid version includes at least one period (.) whereas a hash does not and we
    # can use it to easily differentiate a package version from a commit id/hash.
    # Commit ids are 40 characters long. Using the full hash will yield a long directory
    # names and paths which can be hard to follow while debugging. Therefore, we will
    # use only the first 8 characters of the commit hashes which should (not guaranteed
    # but the chances are rare) identify the commit uniquely.
    if '.' not in version:
        version = version[:8]

    # formulate the path to the config file for the conda environment
    env_file_path = f'conda/configs/{repo}/{version}.yml'

    # Check if the config file instructs to install (`install_repo=True`) the repository as a dependency.
    # By default, do not install the repository.
    install_repo = False
    # Read the config file.
    with open(env_file_path, 'r') as f:
        config = yaml.safe_load(f)
    # Follow the value of `install_repo` if stated in the config file
    if 'install_repo' in config:
        install_repo = config['install_repo']
        # If the config file instructs NOT to install the repository as a dependency but the user instructs
        # only to install the repository on the existing conda environment, return as there is nothing to do.
        if install_repo_only and not install_repo: return
        # `install_repo` is a custom key that is unknown to conda and will throw a warning (or maybe an error
        # in the future). To prevent that, create a temporary YAML config file without the `install_repo` key.
        del config['install_repo']
        env_file_path = 'conda/temp.yml' # overriding
        with open(env_file_path, 'w') as f:
            yaml.safe_dump(config, f)

    # Create a conda environment with the config file unless forbade by the user.
    if not install_repo_only:
        # Create a conda environment
        print('Creating conda environment...'.ljust(35), end='', flush=True)
        command = f'conda env create -p {env_path} -f {env_file_path} --force --quiet --json'
        cp = sp.run(command, shell=True, capture_output=True, text=True)
        # Delete the temporary config file, if one was created
        if env_file_path.endswith('/temp.yml'): os.remove(env_file_path)
        # Inspect conda output to check if the environment is created successful.
        try:
            # Parse conda output as JSON. Though we asked conda to format the output as JSON,
            # sometimes conda prints warnings before the JSON string.
            out = json.loads(cp.stdout[cp.stdout.find('{'):])
            if 'success' in out and out['success']:
                print('[Done]', flush=True)
            # Raise an error to print the conda output
            else: raise
        except:
            # Print failed status followed by stdout and stderr with horizontal separators and return
            print_output(cp)
            return

    # Check if the repository needs to be installed
    if install_repo:
        # Install the repository in the conda environment using pip
        print(f'Installing {repo}...'.ljust(35), end='', flush=True)
        repo_path = os.path.sep.join(['repos', repo, ''])
        cp = run_command(f'pip install {repo_path}', shell=True, env=env_path, capture_output=True, text=True)
        # cp = sp.run(f'pip install {repo_path}', shell=True, env={'CONDA_PREFIX': env_path, 'PATH': os.pathsep.join([os.path.join(env_path, 'bin'), os.environ['PATH']])}, capture_output=True, text=True)
        # Print stdout plus stderr and return if the repository is NOT installed successfully.
        if cp.returncode != 0:
            print_output(cp)
            return
        print('[Done]', flush=True)
    
    # Return `True` to signal the successful execution of all processes.
    return True


def run_test(env_path: str, test_file: str) -> None:
    """
    Runs a Python test file using a conda environment.

    Arguments:
        env_path (str): The path to the conda environment to use.
        test_file (str): The path to the Python test file to execute.
    """
    
    # sp.run(f'python {test_file}', shell=True, env={'CONDA_PREFIX': env_path, 'PATH': os.pathsep.join([os.path.join(env_path, 'bin'), os.environ['PATH']])})
    run_command(f'python {test_file}', shell=True, env=env_path)


# ## Main Methods

def init() -> None:
    """
    Initializes the framework by creating the required directories. This method must be
    executed before the main method to using the framework. This method needs to be
    executed only once. However, subsequent executions will not override anything.
    """

    # List of directories to be created
    dirs = [
        'conda/configs',
        'conda/env/common',
        'repos',
        'test_scripts'
    ]

    # Inform the user about the creation of required directories
    print('Creating required directories:')
    for path in dirs:
        # Create the directory if it does not exist
        # exist_ok=True ensures not to raise any errors if the directory already exists
        os.makedirs(path, exist_ok=True)
        # Inform the user about the created directory
        print(' ', path)


def main(repo: str = None, bug_num: int = None, test_file: str = None, env_readonly: bool = False,
         env_install_repo_only: bool = False, env_persistent: bool = False) -> None:
    """
    Automatically prepares Conda environments and runs saved/given Python scripts to reproduce bugs in packages
    and repositories. The process of preparing the Conda environment includes installing the specific version
    of the package under test and its dependencies from Conda, PyPI and GitHub repositories.

    Arguments:
        repo (str, optional): The name of the repository or Python package under test. If not provided, the repositories will be listed and the user will be prompted to choose one.
        bug_num (int, optional): The specific bug number you want to replicate where 1 indicates the first bug. The bug number corresponds to the sequential order of the bugs listed for the chosen repository. If not provided, the bugs will be listed and the user will be prompted to choose one.
        test_file (str, optional): The path to the Python test script to execute. If not provided or set to None, the user will be prompted. If set to an empty string (''), skips running any test files. If set to 'd', runs the default test file (if one exists). Defaults to None.
        env_readonly (bool, optional): If True, the conda environment will be set to read-only mode. This can be handy to run test files in a customized conda environment. Defaults to False.
        env_install_repo_only (bool, optional): If True, only installs the repository on the existing conda environment. Defaults to False.
        env_persistent (bool, optional): If True, creates a persistent conda environment in a dedicated directory. Otherwise, creates and overrides the conda environment in the "common" directory. Defaults to False.
    """

    # Load the index that contains information on each repo and bug
    # The index file must be formatted as JSON.
    with open('index.json', 'r') as file:
        index = json.load(file)
    
    # helper variables
    hline, ios  = '=' * 80, not repo or not bug_num or test_file is None
    
    # If repo is not provided, list the repositories and prompt the user to choose one
    if not repo:
        print('Select a repository:', flush=True)
        repo_names = list(index.keys())
        for idx, repo in enumerate(repo_names):
            print(f'  {idx+1:2}. {repo}', flush=True)
        repo = repo_names[int(input('Enter the repository id: ')) - 1]
        if not bug_num or not test_file: print(flush=True)
    
    # If the bug number is not provided, list the bugs for the selected repository and prompt the user to choose one.
    if not bug_num:
        print(f'Select a bug from {repo}:', flush=True)
        for idx, bug in enumerate(index[repo]['bugs']):
            # Print the package version or the abbreviated commit hash after the bug/issue title to inform the user
            # if the bug will be replicated using a version of the package from PyPI or a commit from the repository.
            version = bug['version'] if '.' in bug['version'] else bug['version'][:8]
            print(f'  {idx+1:2}. {bug["title"]} ({version})', flush=True)
        bug_num = int(input('Enter the bug number: '))
        if not test_file: print(flush=True)
    bug = index[repo]['bugs'][bug_num - 1]
    
    # Bug id is the corresponding issue id in the GitHub repository. We are using the issue id as it is unique and
    # will not change if the list of bugs is extended in the future.
    bug_id = re.search(r'#(\d+)$', bug['title']).group(1)

    # Check if a default test file exists for the selected bug.
    default_test_file = f'test_scripts/{repo}/{bug_id}.py'
    if not os.path.isfile(default_test_file):
        default_test_file = None
    
    # If the test file is not provided, prompt the user to choose one action from the menu.
    if test_file is None:
        menu = [
            'Choose one of the following:',
            'Input "d" to run the default test script.',
            'Input the path to run a test script.',
            'Press Enter to skip.'
        ]
        # Remove the option to run the default test file from the menu and notify the user if a default test file does not exist.
        if not default_test_file:
            menu.pop(1)
            print('No default test script is provided for this bug.', flush=True)
        print(*menu, sep='\n  - ', flush=True)
        test_file = input('Test script path: ').strip()
    
    # If the user chooses to run the default test script, set `test_file` to `default_test_file`.
    # NOTE: If a default test file does not exist but the user inputs `d`, `test_file` will be set to None which is equivalent to skip.
    if test_file == 'd': test_file = default_test_file
    
    # Separate the input section from the output section with a horizontal line
    if ios: print('\n', hline, '\n', sep='', flush=True)
    
    # Clone the repository if the version is a commit hash.
    if '.' not in bug['version']:
        clone_repo(repo, index[repo]['url'], bug['version'])
    
    # Prepare the conda environment. The environment name (`env_name`) is used to memorize the last prepared environment
    # in the `common` directory and to name the dedicated directories for persistent environments.
    env_name = f'{repo}.{bug["version"]}'
    env_path = f'conda/env/{env_name}' if env_persistent else 'conda/env/common'
    if not env_readonly:
        nf_path, curr_name = f'{env_path}/name.txt', None
        if os.path.isfile(nf_path):
            with open(nf_path, 'r') as f:
                curr_name = f.read().strip()
        if curr_name != env_name:
            # Create a new environment and install dependencies.
            success = prepare_conda_env(env_path, repo, bug['version'], env_install_repo_only)
            if not success: return
            # Save the environment name to a file for later reference.
            with open(nf_path, 'w') as f:
                f.write(env_name)
    
    # Separate the repository and conda environment preparation section from the testing section with a horizontal line
    if not ('.' in bug['version'] and env_readonly) and test_file: print('\n', hline, '\n', sep='', flush=True)

    # Run the test script within the prepared conda environment.
    if test_file: run_test(env_path, test_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Automatically prepares Conda environments and runs saved/given Python scripts to reproduce bugs in packages and repositories. The process of preparing the Conda environment includes installing the specific version of the package under test and its dependencies from Conda, PyPI and GitHub repositories.")

    # Add arguments to the parser
    parser.add_argument('--init', action='store_true', help='Initializes the framework by creating the required directories. This must be the first step to using the framework and needs to be executed only once. However, subsequent executions will not override anything. If set, all other arguments are ignored.')
    parser.add_argument('-r', '--repo', type=str, help='The name of the repository or Python package under test. If not provided, the repositories will be listed and the user will be prompted to choose one.')
    parser.add_argument('-n', '--bug-num', type=int, help='The specific bug number you want to replicate where 1 indicates the first bug. The bug number corresponds to the sequential order of the bugs listed for the chosen repository. If not provided, the bugs will be listed and the user will be prompted to choose one.')
    parser.add_argument('-t', '--test-file', type=str, help='The path to the Python test script to execute. If not provided, the user will be prompted. If set to an empty string (''), skips running any test files. If set to "d", runs the default test file (if one exists).')
    parser.add_argument('--env-readonly', action='store_true', help='If provided, the conda environment will be set to read-only mode. This can be handy to run test files in a customized conda environment.')
    parser.add_argument('--env-install-repo-only', action='store_true', help='If provided, only installs the repository on the existing conda environment.')
    parser.add_argument('-p', '--env-persistent', action='store_true', help='If provided, creates a persistent conda environment in a dedicated directory. Otherwise, creates and overrides the conda environment in the "common" directory.')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Initialize the framework if --init is set
    if args.init:
        init()
    # Otherwise, call the main function with the parsed arguments
    else:
        main(**vars(args))

